#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

class Person(object):

    def __init__(self, name, age, sexuality,nationality,work,salary,specialty):
        self.name = name
        self.age = age
        self.sexuality = sexuality
        self.nationality = nationality
        self.work = work
        self.salary = salary
        self.specialty = specialty

    def talk(self,words):
        print "{0}: \"{1}\"".format(self.name,words)

