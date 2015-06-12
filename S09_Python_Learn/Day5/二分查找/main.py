#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def search(data_set,find_num):
    mid = len(data_set) /2
    if len(data_set) ==1:
        print "cannot find ",find_num
        return
    if data_set[mid] > find_num: #in left
        print 'in left',data_set[:mid]
        search(data_set[:mid],find_num)
    elif data_set[mid] < find_num: #in right
        print 'in right',data_set[mid:]
        search(data_set[mid:],find_num)
    else:
        print "found num",data_set[mid]
if __name__ == '__main__':
    data = range(1,10000,3)
    find = int(raw_input("num:").strip())

    search(data,find)