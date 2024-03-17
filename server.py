import json
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

import utils


class AbsRequestHandler(BaseHTTPRequestHandler):
    def receive(self, params):
        # abstract
        print(json.dumps(params))

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        if self.receive(params):
            self.send_response(200)
            self.end_headers()

    def log_message(self, format, *args):
        # supress any log messages
        return


def reload(data):
    utils.post_to_localhost(
        f'http://localhost:{os.environ["FZF_PORT"]}', data=f"reload({data})"
    )


class RequestHandler(AbsRequestHandler):
    def receive(self, params):
        # サーバリクエストに対する処理を書いていく
        if "reload" in params:
            reload(params["reload"][0])
            return True
        return False


def start():
    httpd = HTTPServer(("", int(os.environ["SERVER_PORT"])), RequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()
