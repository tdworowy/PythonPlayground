import  pika

from RabbitMQ.example1 import connectionInfo


def connect():
    try:
        print("Connecting")

        credentials = pika.PlainCredentials(connectionInfo.get_user_name(), connectionInfo.get_password())
        parameters = pika.ConnectionParameters(connectionInfo.get_ip(),
                                               5672,
                                               '/',
                                               credentials)
        global connection
        connection = pika.BlockingConnection(parameters)
        global channel
        channel = connection.channel()
    except Exception as ex:
        print("Connection failed")
        print(ex)
    else:
        print("Connection succeedd")


def close():
    connection.close()
