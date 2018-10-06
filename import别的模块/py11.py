#!/usr/bin/env python
import random
import string
all_str = string.uppercase+string.digits+string.lowercase
def passwd_create(size=8):

    passwd = ''
    for i in range(int(size)):
        num = random.choice(all_str)
        passwd+=num
    return passwd

if __name__ == '__main__':
    pasize=raw_input('password size : ')
    print passwd_create(pasize)





