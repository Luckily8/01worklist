# -*- coding:utf-8 -*-
# 作用：封装测试报告功能

import time
import unittest
from BeautifulReport import BeautifulReport as bf     # 引入BeautifulReport报告模板


def report_out(test_dir, report_dir, name_project):
    '''
    :test_dir: 用例路径
    :report_dir : 报告路径
    :name_project : 项目名称=>用于报告命名及描述
    :return: 无
    '''

    now = time.strftime("%Y_%m_%d %H_%M_%S")
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')      # 加载测试用例
    report_name = now + '-' + name_project + '_test_report.html'          # 报告名称
    run = bf(discover)
    run.report(filename=report_name, report_dir=report_dir, description=U"upupUI自动化功能回归测试")

    """
    filename:报告名称；
    report_dir：测试报告存放路径；
    description：报告描述；
    """
