#!/usr/bin/env python3.6

f_dst=open('f.py','r')
tmp=f_dst.read()
f_dst.close()

data=eval(tmp)      #转换为对应类型

print('tmp type: %s  data type: %s'%(type(tmp),type(data)))   #tmp字符串类型  #data字典类型


