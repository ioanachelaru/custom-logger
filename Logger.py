import logging


class Logger:
    def __init__(self, process, log_file):
        self.process = process
        self.log_file = log_file

        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - PID %(process)d - %(levelname)s - %(message)s',
                                                    datefmt='%Y-%m-%d %H:%M:%S'))

        self.logger.addHandler(file_handler)


    def log_output(self):
        with open(self.log_file, 'a') as f:
            while True:
                stdout_line = self.process.stdout.readline()
                stderr_line = self.process.stderr.readline()

                if not stdout_line and not stderr_line:
                    return

                if stdout_line:
                    self.logger.info(stdout_line.decode().strip())

                if stderr_line:
                    self.logger.error(stderr_line.decode().strip())
