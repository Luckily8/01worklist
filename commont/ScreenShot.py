# -*- coding:utf-8 -*-
# 作用：封装截图功能并调用

import time

def save_screenshot(Windows):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    pic_path = "../screenshot/"+now+'_screen.png'                           # 保存截图到指定路径
    Windows.get_screenshot_as_file(pic_path)                      # 截图功能

