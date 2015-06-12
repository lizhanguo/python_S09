#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'


import socket
import sys
import os

ip_port = ('127.0.0.1',8000)
sk = socket.socket()
sk.connect(ip_port)

print "\033[33;1m欢迎使用FTP软件，请输入用户名和密码!\033[0m \033[32;1m(The input format:username password)\033[0m"
while True:
    inp = raw_input('\033[32;1mclient:\033[0m')
    sk.send(inp)
    data = sk.recv(1024)
    if data=='no' :
        print '\033[31;1m你输入的用户名和密码不匹配，请重新输入.....\033[0m'
        continue
    while True:
        input = raw_input('\033[32;1m请输入文件路径:\033[0m')
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
    sk.close()

