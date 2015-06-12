#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

from Person import Person
from Car import Car
import time

class Story(object):

    def __init__(self):
        pass


    def wait(self,second):
        time.sleep(second)

    #�����������
    def intro(self):
        John = Person('John',22,'M','China','None','None','Basketball')
        Liz = Person('Liz',22,'F','China','None','None','Dance')
        print "��Ҫ����{0}���и�Ư����Ů���ѽ�{1}�����ǴӸ��������һ������".format(John.name,Liz.name)

    #���鿪ʼ
    def begin(self):
        John = Person('John',22,'M','China','None','None','Basketball')
        Liz = Person('Liz',22,'F','China','None','None','Dance')
        print '''
        ======���¿�ʼ======
        '''
        Liz.talk('�װ��ģ��ҿ����˱�������ѧԺ��')
        s.wait(2)
        John.talk('��û���ϡ����������Ҿ�����׬Ǯ�����ϴ�ѧ��')
        s.wait(2)
        Liz.talk('�������ã���̫������!')

    #������
    def line(self):
        print '''
        ======�����======
        '''

    #���Գ���
    def interview(self):
        Liz = Person('Liz',26,'F','China','None','None','Dance')
        Peter = Person('Peter',32,'M','USA','Manager','30000','Golf')
        car = Car('������')
        print '''
        ======���Գ���======
        '''
        Liz.talk('��ã�����Liz�������ҵļ�����')
        s.wait(2)
        Peter.talk('����������㣬�ܷ������ǹ�˾�����˱�׼����ϲ���Ϊ�����е�һԱ��')
        s.wait(2)
        Liz.talk('�ǳ���л������ʶ��')
        s.wait(2)
        Peter.talk('���ʣ��������ҿ�������ؼ���')
        s.wait(2)
        Liz.talk('�õģ��ǳ���л��')
        s.wait(2)
        print "{0}���ܳ�{1}��{2}�ؼң�".format(Peter.name,car.name,Liz.name)

    #��β����
    def endline(self):
        John = Person('John',31,'male','China','IT CEO','50000','Basketball')
        Liz = Person('Liz',31,'female','China','None','None','Dance')
        print '{0}��Ϊ��xx���ͻ�������˾��{1}����н{2}��'.format(John.name,John.work,John.salary)
        s.wait(2)
        print '{0}�����˷��ͳ���'.format(John.name)
        s.wait(3)
        print 'ĳ��{0}�ڹ�˾��������{1}��'.format(John.name,Liz.name)
        s.wait(2)
        Liz.talk('�þò�����')
        s.wait(2)
        John.talk('�ţ��������')
        s.wait(2)
        Liz.talk('ͦ�õġ��һ������أ����أ�')
        s.wait(2)
        John.talk('��Ҳ�ǣ�')
        s.wait(2)
        Liz.talk('ԭ�����Ҳ��ԣ����������¿�ʼ��')
s = Story()

