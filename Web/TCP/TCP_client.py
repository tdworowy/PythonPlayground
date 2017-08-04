from Web.TCP.TCP_ import TCP

def main1():
    tcp = TCP('127.0.0.1', 65525)
    tcp.clientConect()
    while 1:
        message = input("Message:  ")
        tcp.clientSent(message)

def main2():
    tcp1 = TCP('127.0.0.1', 65524)
    tcp1.clientConect()
    tcp2 = TCP('127.0.0.1', 65525)
    tcp2.clientConect()

    tcp1.clientSent("Test1")
    tcp2.clientSent("Test2")
if __name__ == "__main__":
    main2()
