#!/usr/bin/env python
#_*_encoding:utf-8_*_

__author__ = 'lizhanguo'

import md5
hash = md5.new()
hash.update('admin')
print hash.hexdigest()



import hashlib
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
