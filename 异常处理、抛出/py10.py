#!/usr/bin/env python

import random
import string
all_str = string.ascii_uppercase+string.digits+string.ascii_lowercase
def passwd_create(size=8):

    passwd = ''
    for i in range(int(size)):
        num = random.choice(all_str)
        passwd+=num
    return passwd

if __name__ == '__main__':

    while True:
        try:
            pasize = int(input('password size : '))
            break
        except BaseException as e:
            print('input invalid! please try again...\n',e)
        # finally:
        #     print('ok p
        # lease wait')
    # raise Exception('invalid!',pasize)    #自定义错误
    print (passwd_create(int(pasize)))


