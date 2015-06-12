#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def say(a,b,c):
    print a,b,c
say("hello","zha","tongxue")
def say(a,*args):
    print a,args
say("hello","zha","tongxue")

def say(a,**args):
    print a,args
say("hello",name="alex",age="29")
def say(a,*arg,**args):
   print a,arg,args
say("hello","zha","tongxue",name="alex",age="29")