
import sys
import socket
from threading import Event, Lock, Thread


class ClientThread(Thread):
    def __init__(self,website,sock,sock_addr):
        super(ClientThread,self).__init__()
        self.s = sock
        self.s_addr = sock_addr
        self.website = website

    def __recy_http_request(self):
        data = self.recv_until(self.s, '\r\n\r\n')
        if not data:
            return None
        lines = data.split('\r\n')
        query_tokens = lines.pop(0).split(' ')
        if len(query_tokens) !=3:
            return None

        method,query,cersion = query_tokens
        headers = {}
        for line in lines:
            tokens = line.split(':',1)
            if len(tokens) !=2:
                continue

        header_name = tokens[0].strip().lower()
        header_value = tokens[1].strip()
        headers[header_name] = header_value
        
        if method == 'POST':
          try:
              data_length = int (headers['content-length'])
              data = self.recv_all(self.s, data_length)
          except KeyError as e:
              data = self.recv_remaining(self.s)
          except ValueError as e:
              return None
          else:
              data = None

          request ={
              "method":method,
              "query":query,
              "headers":headers,
              "data":data,
              "client_ip":self.s_addr[0],
              "client_port":self.s_addr[1]
              } 
          return request
      
    def __send_http_response(self,response):
         lines = []
         lines.append('HTTP/1.1 %u %s' % response['status']) 

         lines.append('server: example')
         if 'data' in response:
             lines.append('Content-Length: %u' % len(response['data']))
         else:
             lines.append('Content-Length: 0')
                        
         if 'headers' in response:
             for header in response['headers']: 
                lines.append('%s: %s' % header)
                lines.append('')
         if 'data' in response:
             lines.append(response['data'])

         if sys.version_info.major == 3:
             converted_lines = []
             for line in lines:
                 if type(line) is bytes:
                     converted_lines.append(line)
                 else:
                     converted_lines.append(bytes(line,'utf-8'))
             lines = converted_lines

         self.s.sendall(b'\r\n'.join(lines))


    def __handle_client(self):
        request= self.__recy_http_request()
        if not request:
            sys.stdout.write("[WARNING] Client %s:%i doesn't make any sense."
                             "Disconnecting. \n" % self.s_addr)
            return
            sys.stdout.write("[ INFO ] Client %s:%i requested %s\n" % (self.s_addr[0], self.s_addr[1],request['query']))
            response = self.website.handle_http_request(request)
            self.__send_http_response(response)
    
    def run(self):
        self.s.settimeout(5)
        try:
            self.__handle_client()
        except socket.timeout as e :
            sys.stdout.write("[WARNING] Client %s:%i tomed out. "
                             "Disconnecting. \n" % self.s_addr)
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()

    def recv_until(sock, txt):
        txt =list(txt)
        if sys.version_info.major == 3:
            txt =[bytes(ch,'ascii') for ch in txt ]
        full_data = []
        last_n_bytes = [None] * len(txt)

        while last_n_bytes !=txt:
            next_byte = sock.recv(1)
            if not next_byte:
                return ''
            full_data.append(next_byte)
            last_n_bytes.pop(0)
            last_n_bytes.append(next_byte)
        full_data = b''.join(full_data)
        if sys.version_info.major == 3:
            return str(full_data,'utf-8')
        return full_data

    def recv_all(sock,n):
        data =[]
        while len(data)< n:
            data_latest = sock.recv(n - len(data))
            if not data_latest:
                return None
            data.append(data_latest)
        data = b''.join(data)
        if sys.version_info.major == 3:
            return str(data, 'utf-8')
        return data
    
    def recv_remaining(sock):
        data = []
        while True:
            data_latest = sock.recv(4096)
            if not data_latest:
                data = b''.join(data)
                if sys.version_info.major == 3:
                     return str(data,'utf-8')
                return data
            data.append(data_latest)


