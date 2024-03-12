import os

import requests


def post_to_localhost(*args, **kwargs):
    requests.post(*args, **kwargs, proxies={"http": None})


def refresh_fifo(path):
    os.remove(path)
    os.mkfifo(path)
