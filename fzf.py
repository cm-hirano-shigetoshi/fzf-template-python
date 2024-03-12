import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen

import utils


def get_command_list(server_port, port_publish_path="/tmp/fzf-port"):
    return [
        "fzf",
        "--listen",
        "--bind",
        f"start:execute-silent:echo $FZF_PORT > {port_publish_path}",
        "--bind",
        f'ctrl-a:execute-silent:curl "localhost:{server_port}?reload=date"',
    ]


@dataclass
class Fzf:
    port: int
    proc: Popen

    def __init__(self):
        pass

    def start_asyn(self, server_port, port_publish_path="/tmp/fzf-port"):
        cmd = get_command_list(server_port, port_publish_path)
        utils.refresh_fifo(port_publish_path)
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True)
        with open(port_publish_path) as f:
            self.port = int(f.readlines()[0])

    def communicate(self):
        result = self.proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        return stdout

    def get_port(self):
        return self.port

    def reload(self, data):
        utils.post_to_localhost(f"http://localhost:{self.port}", data=f"reload({data})")
