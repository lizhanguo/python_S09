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


#����nameǰ���#��ȥ�������ӡ������Ϣ��ֱ�Ӵ�ӡ��ȷ����Ϣ