from Handlers.BaseHandler import BaseHandler
import tornado.web
import json


class RegisterHandler(tornado.web.RequestHandler):
    def initialize(self, clients):
        self._clients = clients


    def get(self):
        print 'Hello'
        self.write({ 'WhoIsKing' : '!SHOSTI' })
        self.set_status(200)


    def post(self):
        body = json.loads(self.request.body)

        print body
        user_id =  body['user_id']
        reg_id = body['reg_id']

        if user_id not in self._clients.keys():
            # append new client to the dictionary with its reg_id
            self._clients[user_id] = reg_id

            # send a success response
            self.set_status(200)
            self.write({ 'is_succeed' : True })
        else:
            # send error response
            self.set_status(503)
            self.write({ 'is_succeed' : False })
