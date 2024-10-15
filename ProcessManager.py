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
        self.loggers = []


    def cleanup(self):
        for logger, temp_file in zip(self.loggers, self.temp_files):
            logger.close()
            if logger.can_be_deleted():
                Path(temp_file).unlink()


    def run(self):
        for cmd in self.cmds:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                self.temp_files.append(temp_file.name)

            process_runner = ProcessRunner(cmd)
            process_runner.start()

            logger = Logger(process_runner.get_process(), temp_file.name)
            self.loggers.append(logger)

            thread = threading.Thread(target=logger.log_output)
            thread.start()

            self.threads.append(thread)

        for thread in self.threads:
            thread.join()

        self.cleanup()