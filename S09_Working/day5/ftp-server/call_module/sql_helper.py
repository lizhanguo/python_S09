#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import MySQLdb

import conf #增加此模块，导入conf.py中的内容


class MySqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict #调用conf.py中的conn_dict 赋值

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)

        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#cur = conn.cursor()
        reCount = cur.execute(sql,params)#此值可以判断 sql语句是否执行了
        data = cur.fetchall() #所有记录内容

        cur.close()
        conn.close()
        return data

    def Get_One(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#cur = conn.cursor()
        reCount = cur.execute(sql,params)
        data = cur.fetchone() #取一条记录所有内容
        cur.close()
        conn.close()
        return data

    def Get_Column(self,sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql)
        data = cur.fetchall()

        cur.close()
        conn.close()
        return data

    def Insert_One(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        reCount = cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()

