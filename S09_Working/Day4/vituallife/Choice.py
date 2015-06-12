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
请选择工作：
1.网管（月工资500）
2.餐厅服务员（月工资800）
'''
        ch1 = raw_input('请输入您的选择：').strip()
        if ch1 == '1':
            gl.END1 += 1
            print '{0} 获得了网管的工作！'.format(John.name)
        if ch1 == '2':
            gl.END2 += 1
            print '{0}获得了餐厅服务员的工作！'.format(John.name)
        print '{0}默默的挣钱供liz上学'.format(John.name)

    def choice2(self):
        John = Person('John','22','M','China','None','None','Basketball')
        Liz = Person('Liz','22','F','China','None','None','Dance')
        print '''
        ======电话铃响~~======
请选择：
1.接听
2.不接听
'''
        ch2 = raw_input('请输入您的选择：').strip()
        if ch2 == '1':
            gl.END1 += 1
            Liz.talk('我现在在xxx公司面试，等我的好消息！')
            John.talk('我在家做好饭等你回来庆祝！')
        if ch2 == '2':
            gl.END2 += 1
            print '{0}发来的短信：我现在在xxx公司面试，等我的好消息！'.format(Liz.name)
            John.talk('祝你好运！')

    def choice3(self):
        John = Person('John','22','M','China','None','None','Basketball')
        Liz = Person('Liz','22','F','China','None','None','Dance')
        Peter = Person('Peter','28','M','USA','Manager','30000','Golf')
        print '''
请选择：
1.质问Liz
2.不质问
'''
        ch3 = raw_input('请输入您的选择：').strip()
        if ch3 == '1':
            gl.END1 += 1
            John.talk('约了谁？')
            print '{0}:{1}要带我去打{2}'.format(Liz.name,Peter.name,Peter.specialty)
            John.talk('为什么是他？')
            Liz.talk('他比你有钱比你帅，我不想过这种贫穷的日子了，我们分手吧！')
        if ch3 == '2':
            gl.END2 += 1
            print '{0}：内心很难受！但他默默忍了下来！'.format(John.name)

    #结局判断
    def end_choice(self):
        John = Person('John','22','male','China','None','None','Basketball')
        #选择1的数量大于2，则和好，否则再也不见
        if gl.END1 > gl.END2:
            John.talk('好，我们重新开始！')
        if gl.END1 < gl.END2:
            John.talk('我们已经回不到过去了！再也不见！')