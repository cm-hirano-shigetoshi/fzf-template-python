import os
import socket

import requests


def post_to_localhost(*args, **kwargs):
    requests.post(*args, **kwargs, proxies={"http": None})


def request_fzf(data):
    post_to_localhost(f'http://localhost:{os.environ["FZF_PORT"]}', data=data)


def refresh_fifo(path):
    os.remove(path)
    os.mkfifo(path)


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))  # OSに利用可能なポートを割り当ててもらう
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ポートを再利用可能に設定
        return s.getsockname()[1]  # 割り当てられたポート番号を取得
