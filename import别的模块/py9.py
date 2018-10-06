#!/usr/bin/env python
# coding=utf-8
import sys
import py11
from py8 import nine

def copy(src_name='/home/chen/桌面/python/test',dst_name='/home/chen/桌面/new'):
    f_src= open(src_name)
    f_dst= open(dst_name,'w')
    while True:

        dat=f_src.read(4096)
        if dat == '':
            break
        f_dst.write(dat)

    f_src.close()
    f_dst.close()

# src=raw_input('please input source : ')
# dst=raw_input('please input destination : ')

# copy()
# nine(45)

size=raw_input('please input destination : ')
# py11.all_str='a'
print py11.passwd_create(size)

print 'success!'
