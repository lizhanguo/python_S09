#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'lizhanguo'
import pickle

a = {'100001':['123456',18000],'100002':['456789',15000]}
pickle.dump(a,open('account.pkl','wb'))

goods_list = {'perfume':1000,'macbook':8000,'wine':300,'T-shirt':200,'Suitcase':600}
pickle.dump(goods_list,open('goods.pkl','wb'))
