import  pika

from RabbitMQ.example1 import connectionInfo


def conect():
    try:
        print("Connecting")

        credentials = pika.PlainCredentials(connectionInfo.getUserName(), connectionInfo.getPassword())
        parameters = pika.ConnectionParameters(connectionInfo.getIP(),
                                               5672,
                                               '/',
                                               credentials)
        global connection
        connection = pika.BlockingConnection(parameters)
        global channel
        channel = connection.channel()
    except:
        print("Connection failed")
    else:
        print("Connection succeedd")


def colse():
    connection.close()
