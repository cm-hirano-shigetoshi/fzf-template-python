import os
import subprocess
from dataclasses import dataclass
from subprocess import PIPE, Popen

import core


@dataclass
class Fzf:
    proc: Popen

    def __init__(self):
        pass

    def start_asyn(self):
        cmd = core.get_initial_fzf_cmd(
            os.environ["FZF_PORT"], os.environ["SERVER_PORT"]
        )
        self.proc = subprocess.Popen(cmd, stdout=PIPE, text=True, shell=True)

    def communicate(self):
        result = self.proc.communicate()
        (stdout, stderr) = (result[0], result[1])
        return stdout
