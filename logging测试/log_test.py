#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging
from logging import handlers
#简单的写入文件的log#
# logging.basicConfig(filename='syslog.log',
#                     level=logging.WARNING,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='a')
# logging.warning("hello I'm a warning")

class filter_rule():
    def filter(self,record):
        return 'hello' not in record.getMessage()       #过滤hello
#生成logger对象
logger=logging.getLogger('')
logger.setLevel(logging.WARNING)       #全局等级

#传入过滤类（可以不加）
logger.addFilter(filter_rule())


#生成handler对象，handler决定往哪里输出
c=logging.StreamHandler()        #输出到屏幕
c.setLevel(logging.WARNING)      #设置输出等级

f=handlers.TimedRotatingFileHandler('syslog.log',when='S',interval=3,backupCount=5)     #固定时间
# f=handlers.RotatingFileHandler('syslog.log',maxBytes=200,backupCount=5)       #固定文件大小
f.setLevel(logging.WARNING)

#绑定handler对象到logger
logger.addHandler(c)
logger.addHandler(f)

#生成formatter
c_formatter=logging.Formatter('%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
f_formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

c.setFormatter(c_formatter)
f.setFormatter(f_formatter)

#输出错误
logging.debug("I'm debug")
logging.warning('hello')
logging.error("I'm a error")
logging.error("I'm a error")