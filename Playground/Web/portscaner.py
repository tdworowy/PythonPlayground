from socket import *

from Playground.my_utils.staff.decorators import catch_exception


@catch_exception
def scan_host(host, port,debug=False):
    s = socket(AF_INET, SOCK_STREAM)
    code = s.connect_ex((host, port))
    s.close()
    if debug: print("Port checked: %s response %s" % (port, code))
    return port, code


def _scan_host(hp):
    return scan_host(hp[0], hp[1])


@catch_exception
def scan_ports(host, min, max):
    host_ip = gethostbyname(host)
    print("Host: %s IP: %s" % (host, host_ip))
    print("Scan in progress...")
    results = list(map(_scan_host, [(host, port) for port in range(min, max + 1)]))
    print("Scan Done...")
    return [x[0] for x in results if x[1] == 0]


if __name__ == '__main__':
    open_ports = scan_ports('127.0.0.1', 8080, 8080)
    print("Open Ports:", open_ports)
