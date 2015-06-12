#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import login
import record_type
import shopping

while True:
    user = raw_input('Please input your account:').strip()
    if len(user) == 0:
        continue
    if user == 'exit':
        exit()
    if login.login(user) == 1:
        print 'No this account!'
        continue
    else:
        break
def mainmenu():
    print '''
    ===========================
    Menu:
    1. Shopping
    2. Withdraw
    3. Cashin
    4. Transfer accounts
    5. Search
    6. Exit 
    ============================
    '''

mainmenu()

while True:
    choose = raw_input('Please input your option: ').strip()
    if len(choose) == 0:
        continue
    a = ['1', '2', '3', '4', '5', '6', 'exit']
    if choose not in a:
        print 'Sorry,no this option.Please type again: '
    if choose == '1':
        shopping.shopping(user)
    if choose == '2':
        record_type.withdraw(user)
    if choose == '3':
        record_type.cashin(user)
    if choose == '4':
        record_type.transfer(user)
    if choose == '5':
        record_type.search(user)
    if choose == '6':
        break
    if choose == 'exit':
        break
