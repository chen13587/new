#!/usr/bin/env python3.6
import json

f=open('tmp.json','r')
data=json.load(f)

print(type(data))
print(data)
