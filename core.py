import shlex

import utils

sources = {"initial": "fd", "ctrl-a": "date"}
binds = {"ctrl-a": "reload(date)"}


def get_initial_fzf_cmd(fzf_port, server_port):
    cmd_list = [
        sources["initial"],
        "|",
        "fzf",
        "--listen",
        fzf_port,
        "--bind",
        shlex.quote(
            f'ctrl-a:execute-silent:curl "localhost:{server_port}?bind=ctrl-a"'
        ),
    ]
    with open("/tmp/aaa", "a") as f:
        print(" ".join(cmd_list), file=f)
    return " ".join(cmd_list)


def bind(key):
    utils.request_fzf(data=binds[key])
