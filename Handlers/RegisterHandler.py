from Handlers.BaseHandler import BaseHandler


class RegisterHandler(BaseHandler):
    def post(self):
        # TODO: add body parsing with ID and RegID
        # TODO: add them as key and value to a global dict
        print 'Hello!'
        self.set_status(200)
