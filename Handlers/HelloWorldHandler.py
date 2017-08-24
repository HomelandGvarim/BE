import tornado.ioloop
import tornado.web
from Handlers.BaseHandler import BaseHandler


class HelloWorldHandler(BaseHandler):
    def get(self):
        self.set_status(200)
        print 'haaa'
        self.write("Hello World!")


    def post(self):
        print 'Hello!'
        self.set_status(200)
