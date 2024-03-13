import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen

import utils


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
    port: int
    proc: Popen

    def __init__(self, port):
        self.port = port

    def start_asyn(self, server_port):
        cmd = get_command_list(self.port, server_port)
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True)

    def communicate(self):
        result = self.proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        return stdout

    def get_port(self):
        return self.port

    def reload(self, data):
        print(f"http://localhost:{self.port}")
        utils.post_to_localhost(f"http://localhost:{self.port}", data=f"reload({data})")
