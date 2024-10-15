import logging
from Utils import read_from_csv

STDOUT_FILTERS_FILE = 'filters.csv'


class Logger:
    def __init__(self, process, log_file):
        self.process = process
        self.log_file = log_file
        self.found_warning_or_error = False
        self.stdout_filters = read_from_csv(STDOUT_FILTERS_FILE)

        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)
        self.file_handler = self._setup_file_handler(log_file)
        self.console_handler = self._setup_console_handler()

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    def _setup_file_handler(self, log_file):
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

        return file_handler

    def _setup_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        console_handler.addFilter(
            lambda record: any(keyword in record.getMessage().lower() for keyword in self.stdout_filters))

        return console_handler

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
        log_message = f'PID {self.process.pid} - {stderr_line.decode().strip()}'
        if "warning" in decoded_line:
            self.logger.warning(log_message)
        else:
            self.logger.error(log_message)

    def can_delete_logfile(self):
        return not self.found_warning_or_error

    def close(self):
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()
        self.logger.removeHandler(self.console_handler)