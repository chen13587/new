#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from socket import *
import threading


def send_thread(socked):
    print('发送任务创建成功')
    while True:
        try:
            str=input("Putin data 'q' to break: \n")
            if str =='q':
                socked.close()
                break
            socked.send(str.encode('utf-8'))
        except BaseException as e:
            print('发送失败')
            print(e)
            socked.close()
            break

def recv_thread(socked):
    print('接收任务创建成功')
    while True:
        try:
            data = socked.recv(1024).decode('utf-8')
            print('receive: ', data)
        except BaseException as e:
            print('断开连接')
            print(e)
            socked.close()
            break

def connect():
    ip=input('IP: ')
    port=input('PORT: ')
    print('Connecting for IP: %s PORT: %s...'%(ip,port))
    if port and ip:
        try:
            socked=socket(AF_INET,SOCK_STREAM)
            socked.connect((ip,int(port)))
            thread1=threading.Thread(target=send_thread,args=(socked,))
            thread1.start()
            thread2=threading.Thread(target=recv_thread,args=(socked,))
            thread2.start()
            print('已连接')
        except BaseException as e:
            print('连接失败')
            print(e)

connect()




