#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import MySQLdb

import conf #���Ӵ�ģ�飬����conf.py�е�����


class MySqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict #����conf.py�е�conn_dict ��ֵ

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)

        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#cur = conn.cursor()
        reCount = cur.execute(sql,params)#��ֵ�����ж� sql����Ƿ�ִ����
        data = cur.fetchall() #���м�¼����

        cur.close()
        conn.close()
        return data

    def Get_One(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#cur = conn.cursor()
        reCount = cur.execute(sql,params)
        data = cur.fetchone() #ȡһ����¼��������
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

