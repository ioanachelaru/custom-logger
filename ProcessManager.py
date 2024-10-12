import tempfile
import threading
from pathlib import Path

from Logger import Logger
from ProcessRunner import ProcessRunner

# Set the temp directory to root dir of current project
tempfile.tempdir = Path(__file__).parent

class ProcessManager:
    def __init__(self, cmds):
        self.cmds = cmds
        self.threads = []
        self.temp_files = []

    def run(self):
        for cmd in self.cmds:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            self.temp_files.append(temp_file.name)

            process_runner = ProcessRunner(cmd)
            process_runner.start()

            logger = Logger(process_runner.get_process(), temp_file.name)
            thread = threading.Thread(target=logger.log_output)
            thread.start()

            self.threads.append(thread)

        for thread in self.threads:
            thread.join()