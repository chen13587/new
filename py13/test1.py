#!/usr/bin/env python3.6
#高阶函数 函数可以接收另一个函数作为参数
def func(v):
    return abs(v)
def output(a):
    print(a)

output(func(-5))