#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print "%s is runnig" % self.name
    def speak(self,meg):
        print "%s : %s" %(self.name,meg)

p1=Person('zhongyi',23)
p2=Person('huangdong',35)

p1.run()
p1.speak('hello,huangdong...')

p2.run()
p2.speak('sb')