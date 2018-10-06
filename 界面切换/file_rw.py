#!/usr/bin/env python3.6

#以下有多种读写文件的方法

'''
def read_data():
    f = open('f_data.py','r')
    # f.seek(5)
    data = eval(f.read())
    f.close()
    return data

def write_data(data):
    f = open('f_data.py','w')
    f.write(str(data))
    f.close()
'''

import json

def read_data():
    f=open('tmp.json','r')
    data=json.load(f)       #读取出来的数据已经被json转换为对应格式，相当于执行了eval()
    f.close()
    return data

def write_data(data):
    f = open('tmp.json', 'w')
    json.dump(data, f)
    f.close()