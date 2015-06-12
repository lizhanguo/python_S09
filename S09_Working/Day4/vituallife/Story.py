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

    #主角任务介绍
    def intro(self):
        John = Person('John',22,'M','China','None','None','Basketball')
        Liz = Person('Liz',22,'F','China','None','None','Dance')
        print "主要人物{0}，有个漂亮的女朋友叫{1}。他们从高中起就是一对恋人".format(John.name,Liz.name)

    #剧情开始
    def begin(self):
        John = Person('John',22,'M','China','None','None','Basketball')
        Liz = Person('Liz',22,'F','China','None','None','Dance')
        print '''
        ======故事开始======
        '''
        Liz.talk('亲爱的！我考上了北京城市学院了')
        s.wait(2)
        John.talk('我没考上。。。不过我决定打工赚钱供你上大学！')
        s.wait(2)
        Liz.talk('你对我真好，我太爱你了!')

    #过渡线
    def line(self):
        print '''
        ======四年后======
        '''

    #面试场景
    def interview(self):
        Liz = Person('Liz',26,'F','China','None','None','Dance')
        Peter = Person('Peter',32,'M','USA','Manager','30000','Golf')
        car = Car('法拉利')
        print '''
        ======面试场景======
        '''
        Liz.talk('你好，我是Liz，这是我的简历！')
        s.wait(2)
        Peter.talk('不错，你很优秀，很符合我们公司的用人标准！恭喜你成为我们中的一员！')
        s.wait(2)
        Liz.talk('非常感谢您的赏识！')
        s.wait(2)
        Peter.talk('请问，我有荣幸开车送你回家吗？')
        s.wait(2)
        Liz.talk('好的，非常感谢！')
        s.wait(2)
        print "{0}开跑车{1}送{2}回家！".format(Peter.name,car.name,Liz.name)

    #结尾剧情
    def endline(self):
        John = Person('John',31,'male','China','IT CEO','50000','Basketball')
        Liz = Person('Liz',31,'female','China','None','None','Dance')
        print '{0}成为了xx大型互联网公司的{1}，月薪{2}！'.format(John.name,John.work,John.salary)
        s.wait(2)
        print '{0}购买了房和车！'.format(John.name)
        s.wait(3)
        print '某天{0}在公司外遇到了{1}！'.format(John.name,Liz.name)
        s.wait(2)
        Liz.talk('好久不见！')
        s.wait(2)
        John.talk('嗯，最近好吗？')
        s.wait(2)
        Liz.talk('挺好的。我还单着呢！你呢？')
        s.wait(2)
        John.talk('我也是！')
        s.wait(2)
        Liz.talk('原来是我不对，我们能重新开始吗？')
s = Story()

