from socket import *

from MyUtils.decorators import catch_exception


@catch_exception
def scanHost(host, port):
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))
        s.close()
        print("Port checked: %s response %s" % (port,code))
        return port, code

def scanHost_(hp):
    return scanHost(hp[0],hp[1])

@catch_exception
def scanPorts(host,min,max):
    hostip = gethostbyname(host)
    print("Host: %s IP: %s" % (host, hostip))
    print("Scan in progress...")
    results = list(map(scanHost_,[(host,port)for port in range(min, max+1)]))
    print("Scan Done...")
    return [x[0] for x in results if x[1] == 0 ]


if __name__ == '__main__':
    openPorts = scanPorts('127.0.0.1',8080,8080)
    print("Open Ports:",openPorts)



