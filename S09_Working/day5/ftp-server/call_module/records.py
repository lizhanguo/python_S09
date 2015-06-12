#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import time

from sql_helper import MySqlHelper


class Records:

    def __init__(self):
        self.__helper = MySqlHelper()

    def is_valid_date(self,client_input):
        try:
            time.strptime(client_input,"%Y-%m-%d")
            return 'ok'
        except:
            return 'none'

    def Insert_records(self,username,client_operation_content,date_time):
        sql = "insert into ftp_record (username,client_operation_content,date_time) values (%s,%s,%s);"
        params = (username,client_operation_content,date_time)
        return self.__helper.Insert_One(sql,params)

    def Query_records(self,username,query_date):
        sql = "select * from chat_record where username=%s and date_time>%s and date_time<%s"
        params = (username,query_date,query_date+86400)
        return self.__helper.Get_Dict(sql, params)

