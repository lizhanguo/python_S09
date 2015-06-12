#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def say():
    #name = "lizhanguo"
    try:
        print  name
        print 'hello world'
    except NameError as e:
        print e.message
        print Exception,e
    else:
        print 'Has name'
    finally:
        print "get to finally"

say()


#上面name前面的#号去掉不会打印报错信息，直接打印正确的信息