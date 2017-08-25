import tornado.ioloop
import tornado.web

from Handlers.RegisterHandler import RegisterHandler
from Handlers.FollowersHandler import FollowersHandler


class WebServer(object):
    def __init__(self, port, address, clients, database):
        """
        :param port: Port to listen on for Web Requests
        :param address: local host
        :param clients: runtime array of registered clients
        :param database: database connection
        """
        self._port = port
        self._address = address

        # all requests will be handled as register requests
        self._app = tornado.web.Application([
            (r'/register', RegisterHandler, dict(clients = clients)),
            (r'/follow', FollowersHandler, dict(database = database))
        ])

        # clients dictionary with their RegIDs
        self._clients = clients


    def start(self):
        self._app.listen(self._port, self._address)
        tornado.ioloop.IOLoop.current().start()
