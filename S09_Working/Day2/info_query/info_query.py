#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'
while True:
    query = raw_input("��������Ҫ��ѯ����Ϣ��")
    f=file('staff_info.txt','r')
    for line in f.xreadlines():
        if query in line:
            print line.replace(query,'\033[31;1m%s\033[0m'% query)

    judge = raw_input("�Ƿ��������ѯ��(y/no)").strip()
    if judge == "y":
        continue
    else:
       break
