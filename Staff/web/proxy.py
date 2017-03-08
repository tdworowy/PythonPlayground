import _thread
import socket
import sys


def proxy_thread(conn):
   maxData= 4096
   request =str(conn.recv(maxData))
   print(request)
   first_line = request.split('n')[0]
   print("first_line:", first_line)
   url = first_line.split(' ')[1]
   print("URL:", url)

   if ":" in url[5:] :
       print("Found")
       port_pos = url.find(":") #TODO CHECK
   else: port_pos =-1

   print("port_pos: ",port_pos)
   webserver_pos = url.find("/")
   print("webserver_pos: ",webserver_pos)
   webserver = ""

   if (port_pos==-1 or webserver_pos < port_pos):
    port = 80
    webserver = url[:webserver_pos] #TODO
   else:
     port = int((url[(port_pos+1):])[:webserver_pos-port_pos-1])
     webserver = url[:port_pos]

     print ("Connect to:", webserver, port)

   try:

     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((webserver, port))
     s.send(request)

     while 1:
         data = s.recv(maxData)

         if (len(data) > 0):

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
        print ("Runtime Error:", message)
        sys.exit(1)



def main():

  host = "localhost"
  port = 8000

  try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(50)

  except Exception as message:
        if s:
            s.close()
        print ("Could not open socket:", message)
        sys.exit(1)


  while 1:
    conn, client_addr = s.accept()
    _thread.start_new_thread(proxy_thread, (conn,))



if __name__ == '__main__':
  main()