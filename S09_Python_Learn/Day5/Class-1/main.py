#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

class School(object):
    address = "WuDaoKou"
    master = "Alex"
class SchoolMember(object):
    school_name = "OldBoy IT"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def introduction(self,msg):
        print """
            Hi,my name is %s,I am %s years old.
        %s
       """%(self.name,self.age,msg)
class Student(School,SchoolMember):
    def __init__(self,name,age,sex,class_name,course):
        SchoolMember.__init__(self,name,age,sex)
        self.class_name = class_name
        self.course = course
    def pay_tuition(self,amount):
        print "paving %s to school %s" %(amount,self.address)
class Teacher(SchoolMember):
    def __init__(self,name,age,sex,class_name,course,salary):
        SchoolMember.__init__(self,name,age,sex)
        self.class_name = class_name
        self.course = course
        self.salary = salary
    def teaching(self,content):
        print "teaching %s" %content

s1 = Student('HuangDong',40,'F','s9','Python')
s1.introduction('hahaha zha sb')
s1.pay_tuition(8000)
print s1.class_name,s1.course

t1 = Teacher("Alex",20,"M",'s9',"python",500)
t1.introduction("I am teachers")
t1.teaching("OOP")