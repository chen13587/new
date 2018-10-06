#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import shelve

# data_list=['a','b','c','d']
# data_dict={'cpl':'135','yxy':'110'}

# f=shelve.open('tmp')

# f['abc']=data_list      #以字典格式，存入数据
# f['contacts']=data_dict
#
# f.close()

f=shelve.open('tmp')
a=f['contacts']
print(str(a))

