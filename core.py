import shlex

import utils

sources = {"initial": "fd", "ctrl-a": "date", "ctrl-b": "env"}
binds = {
    "ctrl-a": f'reload({sources["ctrl-a"]})',
    "ctrl-b": f'reload({sources["ctrl-b"]})',
}


def get_bind_potions(server_port):
    options = []
    for key in binds.keys():
        options.append("--bind")
        options.append(
            shlex.quote(
                f'{key}:execute-silent:curl "localhost:{server_port}?bind={key}"'
            )
        )
    return options


def get_initial_fzf_cmd(fzf_port, server_port):
    cmd_list = [
        sources["initial"],
        "|",
        "fzf",
        "--listen",
        fzf_port,
    ] + get_bind_potions(server_port)
    return " ".join(cmd_list)


def bind(key):
    utils.request_fzf(data=binds[key])
