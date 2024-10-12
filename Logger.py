class Logger:
    def __init__(self, process, log_file):
        self.process = process
        self.log_file = log_file

    def log_output(self):
        with open(self.log_file, 'a') as f:
            while True:
                stdout_line = self.process.stdout.readline()
                stderr_line = self.process.stderr.readline()

                if not stdout_line and not stderr_line:
                    break

                if stdout_line:
                    f.write(stdout_line.decode())

                if stderr_line:
                    f.write(stderr_line.decode())