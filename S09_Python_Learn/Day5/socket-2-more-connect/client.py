#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import socket

host = '127.0.0.1'
port = 50002
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    msg = raw_input("client:").strip()
    s.sendall(msg)
    data = s.recv(1024)
    print "server:%s" %data
s.close()