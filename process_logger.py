import subprocess
import threading
import time
import tempfile
from pathlib import Path

# Set the temp directory to root dir of current project
tempfile.tempdir = Path(__file__).parent


def run_process(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process


def log_output(process, log_file):
    while True:
        line = process.stdout.readline()
        if not line:
            break
        with open(log_file, 'a') as f:
            f.write(line.decode())
        print(line.decode(), end='')

def main():
    cmds = [
        """python -c "import sys, time; print('Starting'); sys.stderr.write('Warning: this is a test\\n'); time.sleep(1); print('A process'); sys.stderr.write('Error: something went wrong\\n'); time.sleep(1); print('Finishing')" """,
        """python -c "import sys, time; print('Another start'); sys.stderr.write('Another warning\\n'); time.sleep(2); print('Another process'); sys.stderr.write('Another error message\\n')" """
    ]

    # Store the threads we're about to start
    threads = []

    tmp_files = []

    for cmd in cmds:
        tmp_file = tempfile.NamedTemporaryFile(delete=False)
        tmp_files.append(tmp_file.name)

        process = run_process(cmd)

        thread = threading.Thread(target=log_output, args=(process, tmp_file.name))
        thread.start()

        threads.append(thread)

    # Wait for all threads to finish instead of sleeping,
    # which would've not guaranteed synchronization
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()