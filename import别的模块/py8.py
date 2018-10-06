#!/usr/bin/env python
# coding=utf-8

def nine(num=9):
  for i in range(1,num+1):
    for t in range(1,i+1):
      print '%d×%d=%d' % (t,i,i*t),
    print

if __name__ == '__main__':
  num= int(raw_input('please input num : '))
  nine(num)