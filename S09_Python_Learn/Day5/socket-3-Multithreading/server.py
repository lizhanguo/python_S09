#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import  SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        print self.request,self.client_address,self.server
        while True:
            data = self.request.recv(1024)
            print "recv:%s,%s" %(self.client_address,data)
            self.request.send(data.upper())
    def finish(self):
        pass
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()