#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

from Person import Person
from Car import Car
from School import School
from Story import Story
from Choice import Choice
import gl
import time

#������ʼ
if __name__ == '__main__':
    #��ʼ��������
    story = Story()
    John = Person('John',22,'M','China','None','None','Basketball')
    Liz = Person('Liz',22,'F','China','None','None','Dance')
    Peter = Person('Peter',28,'M','USA','Manager','30000','Golf')
    car = Car('������')
    choice = Choice()
    school = School()

    #���ǽ���
    story.intro()
    story.wait(5)
    #���¿�ʼ
    story.begin()
    #����ѡ��
    choice.choice1()
    story.wait(5)
    story.line()
    story.wait(5)
    John.age = John.age + 4
    Liz.age = Liz.age + 4
    choice.choice2()
    story.wait(5)
    #�����龰
    story.interview()
    story.wait(5)
    print '''
        ======���ʵ�һ��======
    '''
    story.wait(2)
    John.talk('�����ٶ��뼤����ӳ������ȥ���ɣ�')
    story.wait(2)
    Liz.talk('oh!���첻�У���Լ���ˣ�')
    story.wait(5)
    choice.choice3()
    story.wait(5)

    print '''
        ======�����======
    '''
    story.wait(2)
    print '{0}��{1}�����ˣ�{0}�ǳ����ģ��������𣬸ɳ�һ���ɼ�����'.format(John.name, Liz.name)
    story.wait(2)
    John.talk('��һ��ҪŬ�����ϣ�������˦���ң�')
    story.wait(2)
    school.city_college()
    story.wait(2)
    school.oldboy()
    story.wait(2)
    story.line()
    story.wait(2)
    John.age = John.age + 5
    Liz.age = Liz.age + 5
    Peter.age = Peter.age + 5
    #��β����
    story.endline()
    story.wait(2)
    choice.end_choice()

