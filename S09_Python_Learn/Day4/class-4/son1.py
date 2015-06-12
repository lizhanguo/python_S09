#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'
#³éÏó×ÓÀà

from father import Car

class BMW(Car):
    def __init__(self,color,brand):
         Car.__init__(self,color,brand)
    def start(self):
        print "the bmw is starting"
b = BMW('white','bmw')
b.start()
