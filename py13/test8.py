#!/usr/bin/env python3.6

# def __init__(self): 实例化时会调用该函数，一般用来初始化
class Obj():
    def __init__(self):
        print('todo init')
    def output(self):
        print(3333)
obj = Obj()     #将输出‘todo init’
obj.output()




