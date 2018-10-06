#!/usr/bin/env python

# class student:
#     def __init__(self,name,fs):
#         self.name = name
#         self.fs = fs
#
#     def output(self):
#         print(self.name,self.fs)
#
#     def changer(self,num):
#         self.fs+=num
#         print(self.fs)
#
#
# tom=student('tom',20)
# tom.output()
# tom.changer(100)

def b(c):
    return c()+100

@b
def a(i):
    return i


print(a(20))














