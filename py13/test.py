#!/usr/bin/env python
#匿名函数
def func1():
        print('this func1 output')
        def func2():
                print('this func2 output')
        return func2

# print(func1())

f=lambda x,y: x*y if x<y else x/y

print(f(4,8))




