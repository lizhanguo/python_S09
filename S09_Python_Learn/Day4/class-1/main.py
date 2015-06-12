#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

#类的私有属性和私有方法

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        self.__gender = 'male'
        self.__weight = 100
    def say_weight(self):
        print 'my weight is %d'%(self.__weight)
    def __get_a_ax(self):
        return 'AX'
    def chop_woods(self):
        tool = self.__get_a_ax()
        print "%s is chopping woods with %s" %(self.name,tool)
p1=Person('zhongyi',23)
p1.say_weight()
p1.chop_woods()