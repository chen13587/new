#!/usr/bin/env python
num=int(raw_input('please input num: '))-2
str =xrange(num)
i=0
fb=[0,1]
for i in str:
    fb.append(fb[-1]+fb[-2])
print fb