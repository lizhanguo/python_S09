#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

from Person import Person

class School(object):

    def __init__(self):
        pass

    def city_college(self):
        John = Person('John',26,'M','China','None','None','Basketball')
        self.name = '��������ѧԺ'
        print '{0}����һ��ʱ�������{1}���Կ���'.format(John.name,self.name)

    def oldboy(self):
        John = Person('John',26,'M','China','None','None','Basketball')
        self.name = '���к�'
        self.course = 'python'
        print 'ͬʱ{0}�μ��� {1}�� {2}��ѵ�γ̣�'.format(John.name,self.name,self.course)
