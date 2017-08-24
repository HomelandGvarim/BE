from Handlers.BaseHandler import BaseHandler
import tornado.web

class FriendsHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self._db_client = database


    def get(self):
        self.set_status(200)

        db = self._db_client.hackatonDB

        friends = []

        try:
            coll = db.friends.find()
            for friend in coll:
                 friends.append(friend)
        except Exception, e:
            print str(e)

        self.write(str(friends))
