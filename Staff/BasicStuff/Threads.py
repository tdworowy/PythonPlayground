import _thread

def func():
    for i in range(10):
        print(i)



try:
    _thread.start_new_thread( func ,() )
    _thread.start_new_thread( func ,() )
except:
   print ("Error: unable to start thread")

while 1:
    pass