#reciver
from RabbitMQ.example1 import connect
from RabbitMQ.example1 import connectionInfo


def receive(connect):
    connect.channel.queue_declare(queue=connectionInfo.get_python_queue())

    connect.channel.basic_consume(callback,
                                  queue=connectionInfo.get_python_queue(),
                                  no_ack=True)
    print(' [*] Waiting for messages')
    connect.channel.start_consuming()



def callback(ch, method, properties, body):
    print(" Received %r" % body)

conn = connect
conn.connect()
receive(conn)