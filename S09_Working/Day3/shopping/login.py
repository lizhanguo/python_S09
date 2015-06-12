#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'lizhanguo'
import sys
import pickle

def login(user):
    f = file('account.pkl','rb')
    a = pickle.load(f)
    f.close()
    
    lock = [line.strip() for line in open('lock.txt','r').readlines()]    #遍历lock.txt文件并写入lst列表中
    
    error = 0
    if user in lock:
        print '\033[1;31;40m You have been locked forever! Please contact helen@everzones.com! \033[0m'
        exit()

    else:
        if user in a.keys():
            while error<3:    
                p = raw_input('Please type your password:')
                if p == a.get(user)[0]:
                    print 'Welcome to ATM system!'
                    print 'Your balance is: %s'%(a.get(user)[1])
                    break
                else: #密码不正确，错误数加一，并显示剩余输入的密码的机会
                    error += 1
                    print 'Failed! Please enter again! Last %s shots!'%(3-error)    
            else:
                print 'Forbbiden login! Goodbye! Please contact us with this Email: helen@everzones.com.'
                l = open('lock.txt','a')
                l.write(user+'\n')
                l.close()
                exit()
        else:
            return 1
