
class Connection_info:
    def __init__(self, queue):
        # self.ip = "192.168.99.100"
        self.ip = "localhost"
        #self.ip = "192.168.0.101"
        self.queue = queue
        self.user_name = "admin"
        self.password = "admin"
        # self.port = 32770
        self.port = 5672
        self.host = "/"
