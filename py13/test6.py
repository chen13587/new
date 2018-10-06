#!usr/bin/env python3.6
#-*- coding: utf-8 -*-
#不修改原调用方法 来扩展

login_flag = False

def login(typ):
    def outfunc(func):
        def ch(*opt):
            name='1'
            passwd='1'
            global login_flag
            if not login_flag:
                username=raw_input('name: ')
                password=raw_input('passwd: ')
                if (username==name and passwd==password):
                    print('welcome login!')
                    login_flag=True
                else:
                    print('worng name or passwd!')
            else:
                print('验证通过')
            if login_flag:
                func(*opt)
        return ch
    print("please use: %s"%typ)
    return outfunc

# @login
def out(arg):
    print('goto->'+arg)

xx=login('qq')      #偷梁换柱，但不会调用
print(xx)  #out地址为outfunc

out=xx(out)
print(out)      #输出ch函数地址给out

# out('beijin')       #返回的out地址+()就是调用该地址的函数
out('beijin')

