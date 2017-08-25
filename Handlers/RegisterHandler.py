from Handlers.BaseHandler import BaseHandler
import tornado.web
import json


class RegisterHandler(tornado.web.RequestHandler):
    def initialize(self, clients):
        self._clients = clients

    def get(self):
        self.set_status(200)
        print 'Hel'
        self.write('d')

    def post(self):
        body = json.loads(self.request.body)

        id =  body['user_id']
        ip = body['user_ip']
        port = body['user_port']

        if id not in self._clients.keys():
            # append new client to the dictionary with its reg_id
            self._clients[id] = { 'ip' : ip, 'port' : port }

            # send a success response
            self.set_status(200)
            self.write({ 'is_registered' : True })
        else:
            # send error response
            self.set_status(503)
            self.write({ 'is_registered' : False })
