import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """
    Base handler for all handlers.
    """
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')