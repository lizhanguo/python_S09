#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def readlines():
    seek = 0
    while True:
        with open('yield_test.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            print "�ڲ�1============",data,
            if data:
                seek = f.tell()
                print "�ڲ�2============",data,
                yield data
            else:
                return
rf = readlines()
print "�ⲿ1============",rf.next(),
print "�ⲿ2============",rf.next(),
print "�ⲿ3============",rf.next(),

