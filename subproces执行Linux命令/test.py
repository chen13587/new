#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import subprocess

# out_buf=subprocess.run(['ls','-l'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(out_buf.stdout)

# subprocess.run('mkdir atmp',shell=True)
# subprocess.run('ls',shell=True)

a=subprocess.Popen(['ls'],stdout=subprocess.PIPE,cwd='/')
b=subprocess.Popen(['grep','home'],stdin=a.stdout,stdout=subprocess.PIPE)


out=b.stdout.read()

print(out)


