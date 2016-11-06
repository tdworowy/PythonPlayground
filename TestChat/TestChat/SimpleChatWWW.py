import json
import os
import socket
import sys
from threading import Event, Lock, Thread



class SimpleChatWWW():
    def __init__(self, the_end):
        sys.stdout.write("[ INFO ] Simple chat initialization")
        self.the_end = the_end
        self.files = "."
        self.file_cache ={}
        self.file_cache_lock = Lock()
        self.messages = {}
        self.messages_offset = 0
        self.messages_lock = Lock()
        self.messages_limit = 1000

        self.handlers={
            ('GET','/'): self.__handle_GET_index,
            ('GET','/index.html'): self.__handle_GET_index,
            ('GET','/style.css'): self.__handle_GET_style,
            ('GET','/main.js'): self.__handle_GET_javascript,
            ('POST','/chat'): self.__handle_POST_chat,
            ('GET','/,essages'): self.__handle_POST_messages,
            }

    def handle_http_request(self,req):
        req_query=(req['method'],req['query'])
        if req_query not in self.handlers:
            return {'status':(404,'Not Found')}
        return self.handlers[req_query](req)

    def __handle_GET_index(self, req):
        return self.__send_file('httpchat_index.html')

    def __handle_GET_style(self, req):
        return self.__send_file('httpchat_style.css')

    def __handle_GET_javascript(self, req):
        return self.__send_file('httpchat_main.js')


    def __handle_POST_chat(self ,req):
        try:
            obj = json.loads(req['data'])
        except  ValueError:
            return {'status':(400,'Bad request')}
        if type(obj) is not dict or 'text' not in obj:
            return {'status':(400,'Bad request')}
        text = obj['text']
        if type(text) is not str :
            return {'status':(400,'Bad request')}
        sender_ip = req['client_ip']
        with self.messages_lock:
            if len(self.messages) > self.messages_limit:
                self.messages.pop(0)
                self.messages_offset+=1
            self.messages.append((sender_ip,text))

        sys.stdout.write("[ info]<%s> %s\n" % (sender_ip,text))
        return {'status': (200,'OK')}

    def __handle_POST_messages(self ,req):
        try:
            obj=json.loads(req['data'])
        except ValueError:
            return {'status':(400,'Bad request')} 
        if type(obj) is not dict or 'last_message_id' not in obj:
             return {'status':(400,'Bad request')}
        last_massage_id= obj['last_massage_id']
        if type(last_massage_id) is not int:
             return {'status':(400,'Bad request')}

        with self.messages_lock:
            last_massage_id -= self.messages_offset
            if last_massage_id <0:
                last_massage_id =0
            messages = self.messages[last_massage_id:]
            new_last_message_id=self.messages_offset + len(self.messages)

        data = json.dumps({
            "last_message_id":new_last_message_id,
            "messages":messages
            })
        return {
            'status':(200,'OK'),
            'headers':[
                ('Content-Type','application/json;charset=utf-8'),
                ],
            'data':data
            }

    def __send_file(self , fname):
        ext = os.path.splitext(fname)[1]
        mime_type = {
            '.html':'text/html;charset=utf-8',
            '.js':'application/javascript;charset=utf-8',
            '.css':'text/css;charset=utf-8',
            }.get(ext.lower(),'application/octen-stream')

        try:
            mtime = os.stat(fname).st_mtime
        except:
            return {'status':(404 ,'Not found')}

        with self.file_cache_lock:
            if fname in self.file_cache and self.file_cache[fname][0] == mtime:
                return {
                    'status':(200,'OK'),
                    'headers' :[
                        ('Content-Type',mime_type),
                        ],
                    'data':self.file_cache[fname][1]
                    }

            try:
                with open(fname,'rb') as f:
                    data = f.read()
                    mtime = os.fstat(f.fileno().st_mtime)
            except IOError as e:
                   sys.stdout.write("[WARNING] File %s not found , but requested.\n" % fname)
            return {'status':{404 , 'Not Found'}}

        with self.file_cache_lock:
            if fname not in self.file_cache or self.file_cache[fname][0] < mntime:
                self.file_cache[fname] = {mtime ,data}

                return {
                    'status':(200 , 'OK'),
                    'headers':[
                        ('Content-Type',mime_type),
                        ],
                    'data':data
                    }
                

                 






               
