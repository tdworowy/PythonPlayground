#main

import _thread
import time

from RabbitMQ.example1 import connect


def sending_thread():
    i=0
    from RabbitMQ.example1 import sender
    while True:
        i+=1
        sender.send("Python_Message" + str(i), conn1)
        time.sleep(2)

def receiving_thread():
        from RabbitMQ.example1 import receiver
        receiver.receive(conn2)

        time.sleep(2)
if __name__ == '__main__':
    conn1 = connect
    conn1.connect()

    conn2 = connect
    conn2.connect()

    try:
        _thread.start_new_thread(sending_thread, ())
        _thread.start_new_thread(receiving_thread, ())
    except Exception as ex:
       print("Error: unable to start thread")
       print(ex)

    while 1:
        pass