import argparse
import sys

import utils
from fzf import Fzf
from internal_server import InternalServer
from request_handler import RequestHandler as RequestHandlerCls


def main(args, options):
    # ポートを確定させる
    fzf_port = utils.find_free_port()
    server_port = utils.find_free_port()

    # fzfのプロセスを開始
    # 実際は必要なsrcやbindなどをアプリ側で作って渡す
    fzf = Fzf(fzf_port)
    fzf.start_asyn(server_port)

    # serverを起動する
    RequestHandlerCls.set_fzf(fzf)
    server = InternalServer(RequestHandlerCls, server_port)
    server.start()

    # fzfの出力を取得する
    stdout = fzf.communicate()
    print(stdout)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    args = p.parse_args()
    main(sys.argv, args.__dict__)
