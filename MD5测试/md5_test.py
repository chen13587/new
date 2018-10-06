#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import hashlib

with open('msg.py','br') as f:
    a = hashlib.md5()
    str=f.read()

    a.update(str)
    str=a.hexdigest()
    print(str)

