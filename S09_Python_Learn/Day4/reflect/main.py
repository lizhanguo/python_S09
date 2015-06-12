#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import  person

def play(action):
    return getattr(person,action)


action=play('run')
action()
action=play('eat')
action()

