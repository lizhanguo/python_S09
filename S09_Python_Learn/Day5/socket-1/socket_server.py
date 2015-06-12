#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'
import socket
host=''
port = 50001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr = s.accept()
print 'Conected by',addr

while 1:
    data = conn.recv(1024)
    print "%s:%s" %(addr,data)
    reply = raw_input("you:").strip()
    conn.sendall(reply)
conn.close()
