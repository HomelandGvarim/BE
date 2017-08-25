from Handlers.BaseHandler import BaseHandler
import tornado.web
import json


class FollowersHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self._db = database


    def post(self):
        body = json.loads(self.request.body)

        follower = body['follower_id']
        followed = body['followed_id']

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