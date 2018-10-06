#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import re
# f=open('tmp','r')

# for line in f:
#     name,sex,phone=line.split()
#     if phone.isdigit():
#         print(phone)

# data=f.read()
# list=re.findall('1[0-9]{7}',data)
#
# print(type(list))
# print(list)
#
# for i in list:
#     print(i)


# str = 'If you purchase more than 100 sets, the price of product A is $9.90.'
# # num=re.search(r'(\d+).*\$(\d\.?\d*)',str)
# num=re.search('(?P<num>\d+).*\$(?P<money>\d\.?\d*)',str)
# # print('type: %s'%(type(num.groups())),num.groups())
# # print(num.group(1),num.group(2))
# print(num.groupdict())
# print(num['num'])
# print(num['money'])

# str='1356764219@qq.com'
# rule=re.compile('(\w+)@(\w+).(\w+)')
# n=rule.search(str)
# print(n)
# print(n.group(1))
# print(n.group(2))
# print(n.group(3))

rule=re.compile('(\d+).* (\d+)')		#预先编译好规则
n=rule.search('hello cpl 80 age is 70')
print(n.group(2))
