import _thread

def test():
    for i in range(10):
        print()



try:
    _thread.start_new_thread( test ,() )
    _thread.start_new_thread( test ,() )
except:
   print ("Error: unable to start thread")

while 1:
    pass