from Playground.Web.TCP.TCP_ import TCP


def main1():
    tcp = TCP('127.0.0.1', 65525)
    tcp.client_connect()
    while 1:
        message = input("Message:  ")
        tcp.client_sent(message)


def main2():
    tcp1 = TCP('127.0.0.1', 65524)
    tcp1.client_connect()
    tcp2 = TCP('127.0.0.1', 65525)
    tcp2.client_connect()

    tcp1.client_sent("Test1")
    tcp2.client_sent("Test2")


if __name__ == "__main__":
    main2()
