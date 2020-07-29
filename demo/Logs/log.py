import logging
import time
import os
import sys
sys.path.append('..')

from getcwd import get_cwd

'''https://blog.csdn.net/a54288447/article/details/81085714'''

'''封装日志文件'''
def get_log(logger_name):
     #创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

     #设置日志存放路径，日志文件名
        # 获取本地时间，设置时间格式
    rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #设置日志存放路径
    path = get_cwd()
    #通过获取到的路径更新日志路径
    all_log_path = os.path.join(path,'Logs/All_Logs/')
    error_log_path = os.path.join(path,'Logs/Error_Logs/')
    #设置日志名称
    all_log_name = all_log_path + rq + '.log' #以拼接的方式记录文件名称
    error_log_name = error_log_path + rq + '.log'

    #创建handler(日志经办人)
    #创建handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    #写入错误日志
    eh = logging.FileHandler(error_log_name)
    eh.setLevel(logging.ERROR)
    #输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)