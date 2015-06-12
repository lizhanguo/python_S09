#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = 'lizhanguo'

import sys
import time
import pickle


#取现功能函数
def withdraw(user):
    print "Attention: There are 5% fee per withdraw !"
    draw = int(raw_input("Please input how much money you want to withdraw:"))
    f = file('account.pkl','rb')
    a = pickle.load(f)
    f.close()
    balance = a.get(user)[1]
    total_withdraw = draw*1.05
    if balance < total_withdraw:
        print 'Your money is not enough!'
    else:
        balance = balance - total_withdraw
        a.get(user)[1] = balance
        f = file('account.pkl','wb')
        pickle.dump(a,f)
        f.close()
        f = file('account.pkl','rb')
        b = pickle.load(f)
        print 'Withdraw success!'
        print 'Your balance is: %s'%(b.get(user)[1])
        withdraw_write(user,draw)
        return draw
        
#取现操作写入日志函数
def withdraw_write(user,draw):
    tran_time=time.strftime('%Y-%m-%d %H:%M:%S')
    interest = draw*0.05
    record = "credit.log"
    f = open(record,'a')
    f.write("%s    %s    withdraw    -%d    %d\n" %(user,tran_time,draw,interest))
    f.close()

#还款功能函数
def cashin(user):
    money = int(raw_input("Please input how much money you want to cashin:"))
    receivables(user,money)
    f = file('account.pkl','rb')
    b = pickle.load(f)
    print 'Cashin success!'
    print 'Your balance is: %s'%(b.get(user)[1])
    cashin_write(user,money)
    return money

#还款操作写入日志函数
def cashin_write(user,money):
    tran_time=time.strftime('%Y-%m-%d %H:%M:%S')
    record = "credit.log"
    f = open(record,'a')
    f.write("%s    %s    cashin    %d    0\n" %(user,tran_time,money))
    f.close()

#扣款功能函数
def deduct(user,amount):
    f = file('account.pkl')
    a = pickle.load(f)
    if a.get(user)[1] >= int(amount):
        balance = a.get(user)[1] - int(amount)
        a.get(user)[1] = balance
        f.close()
        f = file('account.pkl','wb')
        pickle.dump(a,f)
        f.close()
        return True
    else:
        print 'Your money is not enough!'
        return False    

#收款功能函数
def receivables(user,amount):
    f = file('account.pkl')
    a = pickle.load(f)
    balance = a.get(user)[1] + int(amount)
    a.get(user)[1] = balance
    f.close()
    f = file('account.pkl','wb')
    pickle.dump(a,f)
    f.close()


#转账功能函数
def transfer(user):
    other = raw_input("Please input the each other's account number:").strip()
    amount = int(raw_input('Please input the transfer amount: '))
    cho = raw_input('Are you sure (y/n)?').strip()
    if cho == 'y':
        if deduct(user,amount) == True: #转账方余额减少
            tran_time = time.strftime("%Y-%m-%d %H:%M:%S")
            record = "credit.log"
            f = open(record,'a')
            f.write("%s    %s    transfer    -%d    0\n"%(user,tran_time,amount))
            f.close()
            receivables(other,amount) #收款方，账户余额增加
            cashin_write(other,amount)
            print 'Transfer account success!'
        else:
            print 'Transfer account failed!'
    
def search(user):
    print '========================================================='
    print 'Account    tran_date        tran_type    amount    interest'
    search_file = 'credit.log'
    search_check = file(search_file)  #信用卡操作记录日志
    payment = 0
    interest = 0
    for line in search_check.readlines(): #循环日志文件
        if user in line:
            c = line.split()[4]
            if c[0] == '-':
                payment += int(c.split('-')[1])
                interest += int(line.split()[5])
            else:
                payment -= int(c)
        else:
            continue  #不在line中则跳出此次循环，进入下一行循环判断
    print line    
    print '========================================================='
    print 'Pay: %d    '%payment
    f = file('account.pkl')
    a = pickle.load(f)
    balance = a.get(user)[1]
    print 'Interest: %d    '%interest
    print 'Balance: %d    '%balance    