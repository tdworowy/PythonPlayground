
from TestChat import SimpleChatWWW
from TestChat import serverHTTP
import sys
import socket
from threading import Event


def main():
    the_end = Event()
    website = SimpleChatWWW(the_end)
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('0.0.0.0', 8888))
    s.listen(32)
    s.settimeout(1)

    while not the_end.is_set():
        try:
            c, c_addr = s.accept()
            c.setblocking(1)
            sys.stdout.write("[ INFO ] New Connection %s:%i\n" % c_addr)
        except socket.timeout as e:
            sys.stdout.write("[ ERROR ] %s:%i\n" % e)
            continue
        ct = serverHTTP.ClientThread(website, c, c_addr)
        ct.start()
        
        if __name__ == "__main__":  
            main()
