
class sneder:
    def __init__(self, conect,connectionInfo):
        self.connect = conect
        self.conectionInfo = connectionInfo
    def send (self,message):
        self.connect.getChannel().queue_declare(queue=self.conectionInfo.getQueue())
        self.connect.getChannel().basic_publish(exchange='',
                                              routing_key=self.conectionInfo.getQueue(),
                                              body=message)
        print("Message Sent %r" % message)

    def getQueue(self):
        return self.conectionInfo.getQueue()

