import subprocess

class ProcessRunner:
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def start(self):
        self.process = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get_process(self):
        return self.process