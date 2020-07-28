from Playground.RabbitMQ.example1 import connectionInfo, connect


def send(message, connect):
    connect.channel.queue_declare(queue=connectionInfo.get_java_queue())
    connect.channel.basic_publish(exchange='',
                                  routing_key=connectionInfo.get_java_queue(),
                                  body=message)
    print("Message Sent %r" % message)


if __name__ == '__main__':
    conn = connect
    conn.connect()
    send("Test", conn)
