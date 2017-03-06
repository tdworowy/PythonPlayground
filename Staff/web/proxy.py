import http.server as https
import urllib
from socketserver import ForkingTCPServer #dont work


PORT = 1234

class Proxy(https.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.copyfile(urllib.urlopen(self.path), self.wfile)


httpd = ForkingTCPServer(('', PORT), Proxy) #dont work
print ("serving at port", PORT)
httpd.serve_forever()

#TODO