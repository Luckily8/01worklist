# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 文件名称：logOut.py
# 作用：封装log日志功能

import logging                        # 引入日志模块
import time


def log_out(log_dir, name_project):

    '''
    :log_dir : 日志路径
    :name_project : 项目名称=>用于日志命名
    :return: 无
    '''

    now = time.strftime("%Y_%m_%d %H_%M_%S")   # 获取当前时间，格式：年月日时分秒
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_dir + now + '-' + name_project + '_test_log.log',
                        filemode='w')
    """
    level: 打印日志的级别，INFO：详细； WARNING：警告；ERROR：错误...
    format: 为处理程序使用指定的格式字符串;
    datefmt：使用特定的时间日期格式；
    filename：log日志的文件名称规则；
    filemode：文件读写模式。
    """
