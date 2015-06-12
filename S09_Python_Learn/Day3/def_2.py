#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'


def count():
    for i in range(1,10):
        if i==5:
            return
        else:
            print i
    print "hello world"
res=count()
print res

def count():
    name="lizhanguo"
    for i in range(1,10):
        if i==5:
            return  name
        else:
            print i
    print "hello world"
res=count()
if res=="lizhanguo":
    print "He is a father"