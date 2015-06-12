#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import time

def decorator(func):
    def wrapper(*args,**kargs):
        start= time.clock()
        func(*args,**kargs)
        end = time.clock()
        print "time:%f"%(end - start)
    return wrapper
def output_log(func):
    def wrapper(*args,**kargs):
        print "start %s"%(func)
        func(*args,**kargs)
        print "end %s"%(func)
    return  wrapper


@output_log
@decorator
def say():
    print "I am saying the words"


@output_log
@decorator
def count(a,b):
    print a+b

say()
count(1,2)
