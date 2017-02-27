#main

import _thread
import time

import connect

conn1 = connect
conn1.conect()

conn2 = connect
conn2.conect()

def sedningThread():
    i=0
    import sender
    while(True):
        i+=1
        sender.send("Python_Message" + str(i), conn1)
        time.sleep(2)

def recivingThread():
        import receiver
        receiver.receive(conn2)
        time.sleep(2)


try:
    _thread.start_new_thread( sedningThread,() )
    _thread.start_new_thread( recivingThread, () )
except:
   print ("Error: unable to start thread")

while 1:
    pass