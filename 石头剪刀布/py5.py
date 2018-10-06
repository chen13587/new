#!/usr/bin/env python
# -*- coding:utf8 -*-

import random
all_sel=('石头','剪刀','布')

num=raw_input('''1、石头
2、剪刀
3、布
please select num: ''')
people = all_sel[int(num)-1]
computer=random.choice(all_sel)

win=['石头剪刀','剪刀布','布石头']

if computer == people:
    print '平局'
elif people+computer in win:
    print '你赢了！'
elif people == '石头' or people =='剪刀' or people == '布':
    print '你输了'
else:
    people = '输入无效'
    # print '输入无效'
print '电脑: %s，你: %s' %(computer ,people )