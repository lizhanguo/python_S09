#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import MySQLdb

values=[]
for  i in range(10):
    values.append(('lizhanguo',i,'M'))
print values

conn=MySQLdb.connect(host='localhost',user='root',passwd='hscloud',db='python_test',port=3306)
cur = conn.cursor()
#cur.executemany("insert into student_info (series,name,id,sex) values(%s,%s,%s,%s)",values)
cur.executemany("insert into student_info (name,id,sex) values(%s,%s,%s)",values)

#conn.rollback()  #放在commit之前可以进行回滚（但是会在数据库中会占用序列号）
conn.commit()
#conn.rollback() #放在commit之后就没发回滚了
cur.close()
conn.close()
