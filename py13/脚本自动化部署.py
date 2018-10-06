#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

#脚本自动化部署
import paramiko

def remote_cmd(cmd):
    # 远程执行命令
    stdin,stdout,stderr=ssh.exec_command(cmd)
    output=stdout.read().decode()
    errinfo=stderr.read().decode()
    print(output+errinfo)
    return output+errinfo

#建立连接
ssh=paramiko.SSHClient()    #实例化ssh
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.158',22,'root','5920')   #IP 端口 用户名 密码


output=remote_cmd('ls')
if 'TextInput' in output:
    str=output.split(' ')
    str=[st for st in str if st]
    print(output)
    print(str[1])


# cmd='cat '+stdout.read()
# stdin,stdout,stderr=ssh.exec_command(cmd)
# print(cmd+': '+stdout.read().decode())

# sftp=ssh.open_sftp()
# sftp.put('/home/chen/a.txt','/root/')
# sftp.close()
#退出连接
ssh.close()


