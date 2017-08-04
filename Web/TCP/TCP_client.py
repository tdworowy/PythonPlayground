from Web.TCP.TCP_ import TCP

if __name__ == "__main__":
    tcp = TCP('127.0.0.1', 65524)
    tcp.clientConect()
    while 1:
        message = input("Message:  ")
        tcp.clientSent(message)
