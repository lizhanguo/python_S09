#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def calc_num(n):
    if n / 2 > 0:
        print "%s / 2 =%s" %(n,n/2)
        calc_num(n/2)
calc_num(100)

