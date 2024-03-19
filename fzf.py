import os
import shlex
import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen

SOURCE = "fd"
BIND_KEYS = ["ctrl-a", "ctrl-b"]


def get_initial_fzf_options(fzf_port):
    return [
        "--listen",
        fzf_port,
    ]


def get_bind_potions(server_port, bind_keys):
    options = []
    for key in bind_keys:
        options.append("--bind")
        options.append(
            shlex.quote(
                f'{key}:execute-silent:curl "localhost:{server_port}?bind={key}"'
            )
        )
    return options


@dataclass
class Fzf:
    proc: Popen

    def __init__(self):
        pass

    def start_asyn(self):
        cmd_list = get_initial_fzf_options(os.environ["FZF_PORT"])
        cmd_list += get_bind_potions(os.environ["SERVER_PORT"], BIND_KEYS)
        cmd = " ".join([SOURCE, "|", "fzf"] + cmd_list)
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True, shell=True)

    def communicate(self):
        result = self.proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        return stdout
