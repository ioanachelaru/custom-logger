import logging


class Logger:
    def __init__(self, process, log_file):
        self.process = process
        self.log_file = log_file
        self.found_warning_or_error = False

        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        self.logger.addHandler(file_handler)

    def log_output(self):
        with open(self.log_file, 'a') as f:
            while True:
                stdout_line = self.process.stdout.readline()
                stderr_line = self.process.stderr.readline()

                if not stdout_line and not stderr_line:
                    return

                if stdout_line:
                    self._log_stdout(stdout_line)
                if stderr_line:
                    self.found_warning_or_error = True
                    self._log_stderr(stderr_line)

    def _log_stdout(self, stdout_line):
        self.logger.info(f'PID {self.process.pid} - {stdout_line.decode().strip()}')

    def _log_stderr(self, stderr_line):
        decoded_line = stderr_line.decode().lower()
        if "warning" in decoded_line:
            self.logger.warning(f'PID {self.process.pid} - {stderr_line.decode().strip()}')
        else:
            self.logger.error(f'PID {self.process.pid} - {stderr_line.decode().strip()}')

    def can_be_deleted(self):
        return not self.found_warning_or_error