import os
import tornado.ioloop
import tornado.web
import motor.motor_tornado
from Handlers.HelloWorldHandler import HelloWorldHandler
from Configuration.Config import HOST, PORT, DB_NAME, CONN_STR

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client):
    return tornado.web.Application([
        (r'/helloworld',HelloWorldHandler)])


def main():
    mongo_connection_string = CONN_STR
    mongo_db_name = DB_NAME

    mongo_db_connection = motor.motor_tornado.MotorClient(mongo_connection_string)
    mongo_db_client = mongo_db_connection[mongo_db_name]

    app = create_server_application(mongo_db_client)
    app.listen(port = PORT,address = HOST)
    tornado.ioloop.IOLoop.current().start()



if __name__ == "__main__":
    main()
