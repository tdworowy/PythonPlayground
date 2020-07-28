import datetime
import random
import threading
import time

from RabbitMQ.example2.connect import Connection_
from RabbitMQ.example2.connectionInfo import connection_info
from RabbitMQ.example2.receiver import reciver
from RabbitMQ.example2.sender import sender


def prepare_senders(queues):
    senders = []
    for queue in queues:
        con_info = connection_info(queue)
        connection1 = Connection_(con_info)
        senders.append(sender(connection1, con_info))
    return senders


def prepare_receivers(queues):
    receivers = []
    for queue in queues:
        con_info = connection_info(queue)
        connection1 = Connection_(con_info)
        receivers.append(reciver(connection1, con_info))
    return receivers


def sending_thread(sender):
    while True:
        message = sender.get_queue() + "," + str(random.randrange(1, 10000)) + "," + datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')
        sender.send(message)
        time.sleep(random.uniform(0.05, 4.0))


def receiving_thread(reciver):
    while True:
        reciver.receive()
        time.sleep(random.uniform(0.05, 4.0))


def main():
    queues = ["Queue1", "Queue2", "Queue3"]
    senders = prepare_senders(queues)
    receivers = prepare_receivers(queues)
    flag = True
    while (flag):
        send = input("send :s , recive:r , bouth:b ")
        if send not in ('s', 'r', 'b'):
            print("incorect")
        else:
            flag = False
    try:
        if send in ('s', 'b'):
            for sender in senders:
                threading.Thread(target=sending_thread,
                                 args=(sender,),
                                 ).start()
        if send in ('r', 'b'):
            for reciver in receivers:
                threading.Thread(target=receiving_thread,
                                 args=(reciver,),
                                 ).start()

    except Exception as ex:
        print("Error: unable to start thread")
        print(str(ex))

    while 1:
        pass


if __name__ == "__main__":
    main()
