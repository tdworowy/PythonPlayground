class Sender:
    def __init__(self, connect, connection_info):
        self.connect = connect
        self.connection_info = connection_info

    def send(self, message):
        self.connect.get_channel().queue_declare(queue=self.connection_info.queue)
        self.connect.get_channel().basic_publish(exchange='',
                                                 routing_key=self.connection_info.queue,
                                                 body=message)
        print("Message Sent %r" % message)

    def get_queue(self):
        return self.connection_info.get_queue()
