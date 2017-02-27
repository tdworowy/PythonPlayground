
class conectionInfo:
    def __init__(self, queue):
        # self.ip = "192.168.99.100"
        self.ip = "localhost"
        #self.ip = "192.168.0.101"
        self.queue = queue
        self.userName = "admin"
        self.password = "admin"
        # self.port = 32770
        self.port = 5672
        self.host = "/"

    def getIP(self):
        return  self.ip

    def getQueue(self):
        return self.queue

    def getUserName (self):
        return self.userName

    def getPassword(self):
        return self.password

    def getPort(self):
        return self.port

    def getvHsot(self):
        return self.host