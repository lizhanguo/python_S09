#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

def lizhanguo_downloader(protocol):
    downloader =__import__(protocol+"_downloader")
    downloader.download()

lizhanguo_downloader('http')

lizhanguo_downloader('https')
