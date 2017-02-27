import datetime
import random
import threading
import time

from RabbitMQ.example2.connect import conection_
from RabbitMQ.example2.connectionInfo import conectionInfo
from RabbitMQ.example2.receiver import reciver
from RabbitMQ.example2.sender import sneder


def prepareSenders(queues):
    senders = []
    for queue in queues:
        conInfo = conectionInfo(queue)
        conection1 = conection_(conInfo)
        senders.append(sneder(conection1,conInfo))
    return senders

def prepareRecivers(queues):
    recivers = []
    for queue in queues:
        conInfo = conectionInfo(queue)
        conection1 = conection_(conInfo)
        recivers.append(reciver(conection1,conInfo))
    return recivers


def sedningThread(sender):
    while(True):
        message = sender.getQueue()+","+ str(random.randrange(1, 10000)) +","+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sender.send(message)
        time.sleep(random.uniform(0.05, 4.0))

def receivingThread(reciver):
    while(True):
        reciver.receive()
        time.sleep(random.uniform(0.05, 4.0))


def main():
    queues = ["Queue1", "Queue2", "Queue3"]
    senders = prepareSenders(queues)
    recivers = prepareRecivers(queues)
    flag = True
    while (flag):
        send = input("send :s , recive:r , bouth:b ")
        if send not in ('s','r','b') : print("incorect")
        else: flag = False
    try:
     if(send in ('s','b')):
         for sender in senders:
            threading.Thread(target=sedningThread,
                         args=(sender,),
                         ).start()
     if (send in ('r', 'b')):
        for reciver in recivers:
             threading.Thread(target=receivingThread,
                         args=(reciver,),
                         ).start()

    except Exception as ex:
        print("Error: unable to start thread")
        print(str(ex))

    while 1:
        pass

if __name__ == "__main__":
    main()

