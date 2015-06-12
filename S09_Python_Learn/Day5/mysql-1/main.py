#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='hscloud',db='python_test',port=3306)
    cur = conn.cursor()
    cur.execute('select * from student_info')
    print cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print 'Mysql Error Msg:' ,e