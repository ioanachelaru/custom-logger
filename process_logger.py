import subprocess
import threading
import time

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
    log_files = ['process1.log', 'process2.log']

    for cmd, log_file in zip(cmds, log_files):
        process = run_process(cmd)
        thread = threading.Thread(target=log_output, args=(process, log_file))
        thread.start()

    time.sleep(5)  # Wait for processes to finish

if __name__ == "__main__":
    main()