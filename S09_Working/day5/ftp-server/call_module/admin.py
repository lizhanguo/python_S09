#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'


from sql_helper import MySqlHelper

class Admin(object):

    def __init__(self):
        self.__helper = MySqlHelper() #MySqlHelper()是个实例化后的对象，赋值给 Admin的私有字段__helper
    def CheckValidate(self,userinfo):
        sql = "select * from user_list where username=%s and password=%s"
        params = (userinfo.split()[0],userinfo.split()[1])
        return self.__helper.Get_One(sql,params)