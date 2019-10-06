#sender
from RabbitMQ.example1 import connect
from RabbitMQ.example1 import connectionInfo


def send(message, connect):
    connect.channel.queue_declare(queue=connectionInfo.get_java_queue())
    connect.channel.basic_publish(exchange='',
                                  routing_key=connectionInfo.get_java_queue(),
                                  body=message)
    print("Message Sent %r" % message)


conn = connect;
conn.connect()
send("Test",conn)