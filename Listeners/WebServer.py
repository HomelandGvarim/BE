import os
import tornado.ioloop
import tornado.web

from Handlers.RegisterHandler import RegisterHandler


class WebServer(object):
    def __init__(self, port, address):
        self._port = port
        self._address = address

        # all requests will be handled as register requests
        self._app = tornado.web.Application([ (r'/', RegisterHandler) ])


    def start(self):
        self._app.listen(self._port, self._address)
        tornado.ioloop.IOLoop.current().start()
