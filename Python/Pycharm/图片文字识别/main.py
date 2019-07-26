# coding=utf-8
import keyboard
import time
from PIL import ImageGrab

# object 是所有类的父类


class RecGt(object):
    def screeshot(self):
        if not keyboard.wait(hotkey="ctrl+n"):
            if not keyboard.wait(hotkey="ctrl+c"):
                # 这个ctrl+c 复制图片需要时间，所以要让程序停会。
                time.sleep(0.1)  # 单位秒,0.01秒
                print("已经挂起了0.1秒")
                image = ImageGrab.grabclipboard()
                image.save('test.png')
                # 如果报错 image没有save方法，很可能是image不是图片内容，或者说很可能空


# 使用百度云的产品 人工智能-文字识别 接口
