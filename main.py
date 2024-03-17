import argparse
import os
import sys

import utils
from fzf import Fzf
from internal_server import InternalServer


def main(args, options):
    # ポートを確定させる
    os.environ["FZF_PORT"] = str(utils.find_free_port())
    os.environ["SERVER_PORT"] = str(utils.find_free_port())

    # fzfのプロセスを開始
    # 実際は必要なsrcやbindなどをアプリ側で作って渡す
    fzf = Fzf()
    fzf.start_asyn()

    # serverを起動する
    server = InternalServer()
    server.start()

    # fzfの出力を取得する
    try:
        stdout = fzf.communicate()
        print(stdout, end="")
    finally:
        server.stop()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    args = p.parse_args()
    main(sys.argv, args.__dict__)
