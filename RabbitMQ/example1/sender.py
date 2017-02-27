#sender

import  connect
import  connectionInfo


def send (message, connect):
    connect.channel.queue_declare(queue=connectionInfo.getJavaQueue())
    connect.channel.basic_publish(exchange='',
                                  routing_key=connectionInfo.getJavaQueue(),
                                  body=message)
    print("Message Sent %r" % message)


conn = connect;
conn.conect()
send("Test",conn)