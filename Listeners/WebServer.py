import os
import tornado.ioloop
import tornado.web

from Handlers.RegisterHandler import RegisterHandler


class WebServer(object):
    def __init__(self, port, address, clients):
        self._port = port
        self._address = address

        # all requests will be handled as register requests
        self._app = tornado.web.Application([ (r'/', RegisterHandler, dict(clients = clients)) ])

        # clients dictionary with their RegIDs
        self._clients = clients


    def start(self):
        self._app.listen(self._port, self._address)
        tornado.ioloop.IOLoop.current().start()
