import _thread
import socket

from Playground.my_utils.staff import random_string


class TCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_TCP_server(self, socket_count):
        sockets = []
        for i in range(socket_count):
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.bind((self.host, self.port + i))
            socket_.listen(10)
            sockets.append(socket_)
        while 1:
            for soc in sockets:
                conn, addr = soc.accept()
                print("Conected by", addr)
                data = conn.recv(1024)
                if data:
                    print("Recived", data)
                else:
                    pass

    def client_connect(self):
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.connect((self.host, self.port))

    def client_sent(self, message):
        self.socket_.send(bytes(message, "utf-8"))

    def infinite_sent(self):
        self.client_connect()
        while 1:
            self.client_sent(random_string.generate_random_string(50))


def infinite():
    tcp = TCP("127.0.0.1", 65524)

    try:
        _thread.start_new_thread(tcp.start_TCP_server, ())
        _thread.start_new_thread(tcp.infinite_sent, ())
    except Exception as ex:
        print("Error: unable to start thread")
        print(ex)

    while 1:
        pass


if __name__ == "__main__":
    tcp = TCP("127.0.0.1", 65524)
    tcp.start_TCP_server(2)
