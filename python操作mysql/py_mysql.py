#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
import pymysql

obj=pymysql.connect(host='localhost',user='chen',password='5920',port=3306,charset='utf8')
obj.autocommit(True)       #关闭自动commit
cur=obj.cursor()

try:
    cur.execute('use cpl')

    #插入数据
    name='cpl'
    passwd='123456'
    cur.execute('insert into userinfo ('
                'name,sex,passwd,age,money)'
                'values('
                '"%s",0,"%s",34,2)'%(name,passwd))

    #删除数据
    table='userinfo'
    item='id'
    value=98
    cur.execute("delete from %s where %s = '%s'"%(table,item,str(value)))

    #修改数据
    table = 'userinfo'
    upitem='name'
    newvalue='hi'
    item = 'id'
    value = 99
    cur.execute("update %s set %s = '%s' where %s = '%s'"%(table,upitem,newvalue,item,str(value)))

    #查询数据
    cur.execute('select * from userinfo')
    # cur.execute('delete from userinfo where id>20')


    res=cur.fetchall()
    print('id','name', 'sex', 'passwd', 'age', 'money')
    for a in res:
        id=a[0]
        name=a[1]
        sex=a[2]
        passwd=a[3]
        age=a[4]
        money=a[5]
        print(id,name,sex,passwd,age,money)
    print('execute success')
except BaseException as e:
    obj.rollback()      #出错回滚数据
    print(e)
    print('连接失败')
finally:
    obj.commit()       #commit提交数据
    cur.close()
    obj.close()


