#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import gl
from Person import Person

class Choice(object):

    def __init__(self):
        pass

    def choice1(self):
        John = Person('John','22','M','China','None','None','Basketball')
        print '''
��ѡ������
1.���ܣ��¹���500��
2.��������Ա���¹���800��
'''
        ch1 = raw_input('����������ѡ��').strip()
        if ch1 == '1':
            gl.END1 += 1
            print '{0} ��������ܵĹ�����'.format(John.name)
        if ch1 == '2':
            gl.END2 += 1
            print '{0}����˲�������Ա�Ĺ�����'.format(John.name)
        print '{0}ĬĬ����Ǯ��liz��ѧ'.format(John.name)

    def choice2(self):
        John = Person('John','22','M','China','None','None','Basketball')
        Liz = Person('Liz','22','F','China','None','None','Dance')
        print '''
        ======�绰����~~======
��ѡ��
1.����
2.������
'''
        ch2 = raw_input('����������ѡ��').strip()
        if ch2 == '1':
            gl.END1 += 1
            Liz.talk('��������xxx��˾���ԣ����ҵĺ���Ϣ��')
            John.talk('���ڼ����÷����������ף��')
        if ch2 == '2':
            gl.END2 += 1
            print '{0}�����Ķ��ţ���������xxx��˾���ԣ����ҵĺ���Ϣ��'.format(Liz.name)
            John.talk('ף����ˣ�')

    def choice3(self):
        John = Person('John','22','M','China','None','None','Basketball')
        Liz = Person('Liz','22','F','China','None','None','Dance')
        Peter = Person('Peter','28','M','USA','Manager','30000','Golf')
        print '''
��ѡ��
1.����Liz
2.������
'''
        ch3 = raw_input('����������ѡ��').strip()
        if ch3 == '1':
            gl.END1 += 1
            John.talk('Լ��˭��')
            print '{0}:{1}Ҫ����ȥ��{2}'.format(Liz.name,Peter.name,Peter.specialty)
            John.talk('Ϊʲô������')
            Liz.talk('��������Ǯ����˧���Ҳ��������ƶ��������ˣ����Ƿ��ְɣ�')
        if ch3 == '2':
            gl.END2 += 1
            print '{0}�����ĺ����ܣ�����ĬĬ����������'.format(John.name)

    #����ж�
    def end_choice(self):
        John = Person('John','22','male','China','None','None','Basketball')
        #ѡ��1����������2����ͺã�������Ҳ����
        if gl.END1 > gl.END2:
            John.talk('�ã��������¿�ʼ��')
        if gl.END1 < gl.END2:
            John.talk('�����Ѿ��ز�����ȥ�ˣ���Ҳ������')