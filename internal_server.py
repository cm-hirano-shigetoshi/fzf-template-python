import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen


@dataclass
class InternalServer:
    proc: Popen

    def __init__(self):
        pass

    def start(self):
        cmd = "python server.py"
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True, shell=True)

    def stop(self):
        self.proc.terminate()
