#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import socket
import sys
import os

ip_port = ('127.0.0.1',8000)
sk = socket.socket()
sk.connect(ip_port)
while True:
    input = raw_input('请输入文件路径:')
    cmd,path = input.split()
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send(cmd+'|'+file_name+'|'+str(file_size))

    sent_size = 0
    f = file(path,'rb')
    flag =True
    while flag:
        if sent_size + 4096 >file_size:
            data = f.read()
            flag = False
        else:
            data = f.read(4096)
            sent_size += 4096
        sk.send(data)
    f.close()

