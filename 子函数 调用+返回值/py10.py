#!/usr/bin/env python
import sys

def f(num):
    num+=10
    return num

val=int(raw_input('please input num: '))

a=f(val)

print 'a=%d' % (a)

