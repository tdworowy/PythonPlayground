import _thread
import socket
import sys


def proxy_thread(conn):
    max_data = 4096
    request = conn.recv(max_data)
    request_str = str(request)
    print(request_str)
    first_line = request_str.split("n")[0]
    print("first_line:", first_line)
    url = first_line.split(" ")[1]
    print("URL:", url)
    url2 = url[7:]

    if ":" in url2:
        print("Found")
        port_pos = url2.find(":")
    else:
        port_pos = -1

    print("port_pos: ", port_pos)
    webserver_pos = url2.find("/")
    print("webserver_pos: ", webserver_pos)
    webserver = ""

    if port_pos == -1 or webserver_pos < port_pos:
        port = 80
        webserver = url2[:webserver_pos]  # TODO
    else:
        port = int((url2[(port_pos + 1) :])[: webserver_pos - port_pos - 1])
        webserver = url2[:port_pos]
    print("Connect to:", webserver, port)

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(request)

        while 1:
            data = s.recv(max_data)
            print(str(data))
            if len(data) > 0:
                conn.send(data)
            else:
                break
            s.close()
            conn.close()
    except Exception as message:
        if s:
            s.close()
        if conn:
            conn.close()
        print("Runtime Error:", message)
        sys.exit(1)


def main():
    host = "localhost"
    port = 8080

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(50)

    except Exception as message:
        if s:
            s.close()
        print("Could not open socket:", message)
        sys.exit(1)

    while 1:
        conn, client_addr = s.accept()
        print(conn, client_addr)
        _thread.start_new_thread(proxy_thread, (conn, client_addr))  # TODO Check


if __name__ == "__main__":
    main()
