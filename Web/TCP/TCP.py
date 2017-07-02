import _thread
import socket

from MyUtils import randomString


class tcp:
    def __init__(self, host, port):
        self.host = host
        self.port = port


    def tcpServer(self):
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.bind((self.host, self.port))
        socket_.listen(1)
        conn, addr = socket_.accept()
        print("Conected by", addr)
        while 1:
            data = conn.recv(1024)
            if not data: break
            conn.send(data)
        conn.close()

    def clientConect(self):
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((self.host, self.port))
        return socket_

    def clientSent(self,socket_,message):
         socket_.send(bytes(message, 'utf-8'))
         data = socket_.recv(1024)
         print("Recived", data)

    def infiniteSent(self):
        socket = self.clientConect()
        while 1 :
            self.clientSent(socket, randomString.randomString(50))



def main():
    TCP = tcp('127.0.0.1',65524)

    try:
        _thread.start_new_thread(TCP.tcpServer, ())
        _thread.start_new_thread(TCP.infiniteSent, ())
    except Exception as ex:
        print("Error: unable to start thread")
        print(ex)

    while 1:
        pass




if __name__ == "__main__":
    main()
