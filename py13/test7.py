#!usr/bin/env python3.6
#-*- coding: utf-8 -*-

def mrange(num):
    while num:
        print('num=',num)
        sign=yield num
        print('sign=',sign)
        # if(sign==11):
        #     break
        num-=1
y=mrange(10)

next(y)
next(y)
y.send('hello')

print('end')














