import os
import tornado.ioloop
import tornado.web
from pymongo import MongoClient
from Handlers.HelloWorldHandler import HelloWorldHandler
from Handlers.FriendsHandler import FriendsHandler
from Configuration.Config import HOST, PORT

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client):
    return tornado.web.Application([
        (r'/helloworld', HelloWorldHandler),
        (r'/sample_friends', FriendsHandler, dict(database = mongo_db_client))
    ])


def main():
    mongo_db_client = MongoClient('localhost:27017')

    app = create_server_application(mongo_db_client)
    app.listen(port = PORT, address = HOST)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()