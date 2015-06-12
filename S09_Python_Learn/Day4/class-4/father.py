#!/usr/bin/env python
#_*_encoding:utf-8_*_

#≥ÈœÛ∏∏¿‡
__author__ = 'lizhanguo'
from abc import ABCMeta,abstractmethod

class Car(object):
    __metaclass__ = ABCMeta
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    @abstractmethod
    def start(self):
        pass
