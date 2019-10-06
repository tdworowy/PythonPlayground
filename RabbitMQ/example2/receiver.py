

class reciver:
    def __init__(self, connect, connection_info):
        self.connect = connect
        self.connection_info = connection_info


    def receive(self):
        self.connect.get_channel().queue_declare(queue=self.connection_info.queue)
        self.connect.get_channel().basic_consume(self.callback,
                                                 queue=self.connection_info.queue,
                                                 no_ack=True)

        self.connect.get_channel().start_consuming()




    def callback(self,ch, method, properties, body):
        print("Received %r" % body)


