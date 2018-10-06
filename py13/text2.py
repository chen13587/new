#!/usr/bin/env python3.6
#递归算法
def func(a,n):

    print(a)
    if(n<3):
        return func(a/2,n+1)
    else:
        return a

print(func(10,1))