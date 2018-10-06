#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from socket import *
import threading

c_server=socket(AF_INET,SOCK_STREAM)       #设置为TCP/IPV4
c_server.bind(('',8081))
c_server.listen(10)      #最多同时连接5台

def recv_thread(socked):
    while True:
        data = ''
        try:
            data=socked.recv(1024).decode('utf-8')      #阻塞线程
            print('receive: ',data)
        except BaseException as e:
            print('断开连接')
            print(e)
            socked.close()
            break

def send_thread(socked):
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

print('wait client connect...')

while True:
    print('accept client connect...')
    client,c_addr=c_server.accept()     #阻塞线程
    print('Connect from : ',c_addr)

    thread1=threading.Thread(target=send_thread,args=(client,))
    thread1.start()
    thread2=threading.Thread(target=recv_thread,args=(client,))
    thread2.start()


