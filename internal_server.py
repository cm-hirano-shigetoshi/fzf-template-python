import atexit
import json
import threading
import urllib.parse
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class AbsRequestHandler(BaseHTTPRequestHandler):
    @classmethod
    def set_fzf(cls, fzf):
        cls.fzf = fzf

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


class ThreadedHTTPServer(threading.Thread):
    def set_handler(self, request_handler):
        self.httpd = HTTPServer(("", 0), request_handler)
        return self.httpd.server_port

    def run(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()


@dataclass
class InternalServer:
    server: Thread
    port: int

    def __init__(self, request_handler_cls):
        self.server = ThreadedHTTPServer(daemon=True)
        self.port = self.server.set_handler(request_handler_cls)
        atexit.register(self.server.stop)

    def get_port(self):
        return self.port

    def start(self):
        self.server.start()
