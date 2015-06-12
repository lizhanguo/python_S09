#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import os,sys

while True:
  account_file = file('account.txt')
  account_list = account_file.readlines()
  account_file.close()   # read account tables file , and closed
  lock_file = file('lock.txt')
  lock_list = lock_file.readlines()
  lock_file.close()  #read locked tables file , and closed

  test = False
  username = raw_input('please input username:').strip()   #input username,²¢ÍÑµô¿Õ¸ñ

  for lock_user in lock_list:
    a = lock_user.split()
    if username == a[0]:
       print "%s are locked , you don't login in" % username
       break      # judge user whether or not in locked tables, if in notification user locked

  else:
    for account_user in account_list:
      b = account_user.split()
      if username == b[0]:      # judge user whether or not in account tables
        for i in range(3):   # intput password,circulation 3 times
          password = raw_input('input password:').strip()
          if password == b[1]:
            print 'welcome %s login in' % username
            test = True
            break
          else:
            print 'password is wrong,you have %d times chances,please input correct password,' % (2-i)   # notification you have several times

        else:
            f = file('lock.txt','a')
            f.write('%s\n' % username)    # input 3 times wrong  password ,user are locked
            print 'password is wrong , username %s you has locked' % username
            break
      if test is True:
         sys.exit()
    else:
	add = raw_input('you want to add %s (y/n):' % username)
	if add == 'y':
	   add_password =raw_input('please input add %s password:' % username)
	   add_user=file('account.txt','a')
	   add_user.write('%s %s \n' %(username,add_password) )
	   add_user.flush()
           print 'new user %s add success,please login in again' % username
           continue


