#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = 'lizhanguo'

import time
import pickle

import record_type


def show_title():
    print '''
    ====================================
    1.Buy Goods
    2.Checkout
    3.Exit
    ====================================
    '''
def show_goods_list():
    f = open('goods.pkl')
    goods_list = pickle.load(f)
    f.close()
    print'===================================='
    for k,v in goods_list.items():
        print k+'\t : %d'%v
    print'===================================='
    
#购物车添加商品功能函数
def shopping_car():
    buy_list = []
    while True:
        show_goods_list()
        buy = raw_input("Please choice goods: ").strip()
        f = open('goods.pkl')
        goods_list = pickle.load(f)
        f.close()
        if buy in goods_list.keys():
            select = raw_input('Add to shopping cart?(y/n)').strip()
            if select == 'y':            
                buy_list.append(buy)
                continue
            else:
                return buy_list
                break
        else:
            print 'Without this goods, please input again!'
            continue

#计算购物车中商品总价功能函数    
def shopping_bill(buy_list):
    f = open('goods.pkl')
    goods_list = pickle.load(f)
    f.close()
    count = 0
    for i in buy_list:
        count += goods_list.get(i)
    return count
    
#结账功能函数
def checkout(user,buy_list):
    count = shopping_bill(buy_list)
    print 'You bought these goods: %s'%buy_list
    print 'In your shopping cart commodity prices: %s'%count
    choice = raw_input('Are you sure checkout?(y/n)').strip()
    if choice == 'y':
            if record_type.deduct(user,count) == True:
                tran_time = time.strftime("%Y-%m-%d %H:%M:%S")
                record = "credit.log"
                f = open(record,'a')
                f.write("%s    %s    shopping    -%d    0\n"%(user,tran_time,count))
                f.close()
                print 'Payment is successful!'
            else:
                print 'Payment failed!'
    else:
        print 'Have a nice day, thank you!'    

#购物主程序函数
def shopping(user):
    print '''
    ==============================
    Welcome to shopping mall
    '''
    while True:
        show_title()
        cho = raw_input('Please input your option: ').strip()
        if len(cho) == 0:
            continue
        a = ['1', '2', '3', 'exit']
        if cho not in a:
            print 'Sorry,no this option.Please try again: '
        if cho == '1':
            buy_list = shopping_car()
            print 'The goods you choose are these: %s .Please checkout!'%(buy_list)
        if cho == '2':
            checkout(user,buy_list)
        if cho == '3':
            break
    
