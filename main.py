import argparse
import sys

from fzf import Fzf
from internal_server import InternalServer
from request_handler import RequestHandler as RequestHandlerCls


def main(args, options):
    server = InternalServer(RequestHandlerCls)
    server.start()
    fzf = Fzf()
    fzf.start_asyn(server.get_port())
    RequestHandlerCls.set_fzf(fzf)
    stdout = fzf.communicate()
    print(stdout)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    args = p.parse_args()
    main(sys.argv, args.__dict__)
