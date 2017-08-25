import os
from pymongo import MongoClient
from Configuration.Config import SERVER_HOST, SERVER_PORT, API_KEY, REG_ID

from Listeners.WebServer import WebServer


root = os.path.dirname(__file__)


def main():
    clients = {}
    mongo_db_client = MongoClient('localhost:27017')

    server = WebServer(SERVER_PORT, SERVER_HOST, clients, mongo_db_client)
    server.start()

if __name__ == "__main__":
    main()