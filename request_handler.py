from internal_server import AbsRequestHandler


class RequestHandler(AbsRequestHandler):
    def receive(self, params):
        # サーバリクエストに対する処理を書いていく
        if "reload" in params:
            RequestHandler.fzf.reload(params["reload"][0])
            return True
        return False
