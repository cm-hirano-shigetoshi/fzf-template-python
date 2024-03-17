import os
import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen


def get_command_list(fzf_port, server_port):
    return [
        "fzf",
        "--listen",
        str(fzf_port),
        "--bind",
        f'ctrl-a:execute-silent:curl "localhost:{server_port}?reload=date"',
    ]


@dataclass
class Fzf:
    proc: Popen

    def __init__(self):
        pass

    def start_asyn(self):
        cmd = get_command_list(os.environ["FZF_PORT"], os.environ["SERVER_PORT"])
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True)

    def communicate(self):
        result = self.proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        return stdout
