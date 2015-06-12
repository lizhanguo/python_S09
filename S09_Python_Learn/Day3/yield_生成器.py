#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def readlines():
    seek = 0
    while True:
        with open('yield_test.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            print "内部1============",data,
            if data:
                seek = f.tell()
                print "内部2============",data,
                yield data
            else:
                return
rf = readlines()
print "外部1============",rf.next(),
print "外部2============",rf.next(),
print "外部3============",rf.next(),

