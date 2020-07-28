import logging
import time
import os
#import sys

#sys.path.append('../..') 
import getcwd as getcwd

'''https://blog.csdn.net/a54288447/article/details/81085714'''

'''封装日志文件'''
def get_log(logger_name):
    #创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    #设置日志存放路径，日志文件名
        #获取本地时间，设置时间格式
    rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
