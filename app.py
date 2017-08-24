import os
import tornado.ioloop
import tornado.web
from pymongo import MongoClient
from Handlers.HelloWorldHandler import HelloWorldHandler
from Handlers.FriendsHandler import FriendsHandler
from Configuration.Config import SERVER_HOST, SERVER_PORT, API_KEY, REG_ID

from gcm import GCM

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client):
    return tornado.web.Application([
        (r'/', HelloWorldHandler),
        (r'/sample_friends', FriendsHandler, dict(database = mongo_db_client))
    ])


def _main():
    mongo_db_client = MongoClient('localhost:27017')

    app = create_server_application(mongo_db_client)
    app.listen(port = SERVER_PORT, address = SERVER_HOST)
    tornado.ioloop.IOLoop.current().start()


def main():
    
    gcm = GCM(API_KEY)

    registration_ids = [ 'tok1', 'tok2' ]

    notification = {
        'title' : 'Hello World!',
        'message' : 'Tap to go to Wonderland!'
    }


    response = gcm.json_request(registration_ids = registration_ids,
                                data = notification,
                                collapse_key = 'HELLO_FUCKING_WORLD',
                                delay_while_idle = False)

    if response and 'success' in response:
        for reg_id, success_id in response['success'].items():
            print ''

if __name__ == "__main__":
    main()