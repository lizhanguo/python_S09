#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'
# ���������

class Car(object):
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    def run(self):
        print "The car is running"
    def info(self):
        print "The car is %s %s" %(self.color,self.brand)