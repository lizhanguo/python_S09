#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def send_err_msg(self,msg):
        self.request.send(msg)
    def handle(self):
        path = 'd:/ftp_data'
        while True:
            print self.request,self.client_address,self.server
            data = self.request.recv(1024)
            print data
            data = data.split('|')
            if data[0] == "put":
                if len(data) >2:
                    filename_from_cli,file_size = data[1],int(data[2])
                    self.request.send("ReadyToRecvFileContent")
                    f = file('%s/%s' %(path,filename_from_cli),'wb')

                    recv_size = 0
                    flag = True
                    while flag:
                        if recv_size + 4096 > file_size:
                            recv_data = self.request.recv(file_size - recv_size)
                            flag = False
                        else:
                            recv_data = self.request.recv(4096)
                            recv_size += 4096
                        f.write(recv_data)
                    print "Receving file success!"
                    f.close()
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8000),MyServer)
    server.serve_forever()

