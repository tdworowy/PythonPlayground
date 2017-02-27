

class reciver:
    def __init__(self, conect,connectionInfo):
        self.connect = conect
        self.conectionInfo = connectionInfo


    def receive(self):
        self.connect.getChannel().queue_declare(queue=self.conectionInfo.getQueue())
        self.connect.getChannel().basic_consume(self.callback,
                                      queue=self.conectionInfo.getQueue(),
                                      no_ack=True)

        self.connect.getChannel().start_consuming()




    def callback(self,ch, method, properties, body):
        print("Received %r" % body)


