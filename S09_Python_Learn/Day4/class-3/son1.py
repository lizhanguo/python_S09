#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

from father import Car

class Aodi(Car):
    def __init__(self,color,brand):
        Car.__init__(self,color,brand)
car=Aodi('black','aodi')
car.run()
car.info()