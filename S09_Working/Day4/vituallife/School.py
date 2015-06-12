#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

from Person import Person

class School(object):

    def __init__(self):
        pass

    def city_college(self):
        John = Person('John',26,'M','China','None','None','Basketball')
        self.name = '北京城市学院'
        print '{0}花了一年时间完成了{1}的自考！'.format(John.name,self.name)

    def oldboy(self):
        John = Person('John',26,'M','China','None','None','Basketball')
        self.name = '老男孩'
        self.course = 'python'
        print '同时{0}参加了 {1}的 {2}培训课程！'.format(John.name,self.name,self.course)
