#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
class c():
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print('exec enter')
        return self     #返回自己实例化的对象
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exec exit')
    def out(self):
        print(self.name)

with c('hello cpl') as a:     #a将接收c()类中__enter__方法的返回值，相当于a=c()
    #代码块执行前，将执行一次__enter__方法
    print('----')
    a.out()     #对象a，调用c()中的方法
    print('----')
    #代码块执行完后，将执行一次__exit__方法
