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

#主程序开始
if __name__ == '__main__':
    #初始化各个类
    story = Story()
    John = Person('John',22,'M','China','None','None','Basketball')
    Liz = Person('Liz',22,'F','China','None','None','Dance')
    Peter = Person('Peter',28,'M','USA','Manager','30000','Golf')
    car = Car('法拉利')
    choice = Choice()
    school = School()

    #主角介绍
    story.intro()
    story.wait(5)
    #故事开始
    story.begin()
    #工作选择
    choice.choice1()
    story.wait(5)
    story.line()
    story.wait(5)
    John.age = John.age + 4
    Liz.age = Liz.age + 4
    choice.choice2()
    story.wait(5)
    #面试情景
    story.interview()
    story.wait(5)
    print '''
        ======晴朗的一天======
    '''
    story.wait(2)
    John.talk('今天速度与激情上映，我们去看吧！')
    story.wait(2)
    Liz.talk('oh!今天不行，我约了人！')
    story.wait(5)
    choice.choice3()
    story.wait(5)

    print '''
        ======几天后======
    '''
    story.wait(2)
    print '{0}和{1}分手了！{0}非常伤心，决定奋起，干出一番成绩来！'.format(John.name, Liz.name)
    story.wait(2)
    John.talk('我一定要努力向上，让你后悔甩了我！')
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
    #结尾剧情
    story.endline()
    story.wait(2)
    choice.end_choice()

