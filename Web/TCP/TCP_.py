import _thread
import socket

from MyUtils import randomString


class TCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port


    def startTCPServer(self,socketCount):
        sockets = []
        for i in range(socketCount):
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.bind((self.host, self.port+i))
            socket_.listen(10)
            sockets.append(socket_)
        while 1:
            for soc in sockets:
                conn, addr = soc.accept()
                print("Conected by", addr)
                data = conn.recv(1024)
                if data:
                    print("Recived", data)
                else: pass


    def clientConect(self):
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.connect((self.host, self.port))


    def clientSent(self,message):
        self.socket_.send(bytes(message, 'utf-8'))

    def infiniteSent(self):
        self.clientConect()
        while 1:
            self.clientSent( randomString.generateRandomString(50))



def inifinite():
    tcp = TCP('127.0.0.1',65524)

    try:
        _thread.start_new_thread(tcp.startTCPServer, ())
        _thread.start_new_thread(tcp.infiniteSent, ())
    except Exception as ex:
        print("Error: unable to start thread")
        print(ex)

    while 1:
        pass




if __name__ == "__main__":
    tcp = TCP('127.0.0.1', 65524)
    tcp.startTCPServer(2)
