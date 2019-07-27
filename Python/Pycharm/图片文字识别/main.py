# coding=utf-8
import keyboard
import time
from PIL import ImageGrab

# object 是所有类的父类


class RecGt(object):
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '16898200'
        self.API_KEY = 'EvSWmvXiNoRt3mW2s7ox8KYi'
        self.SECRET_KEY = 'INx9wooqlHnrwRg8vkvQq8MF7y7BH4UG'
        self.FILEPATH='test.png'

    def screeshot(self):
        # 截图使用Windows草图工具
        if not keyboard.wait(hotkey="ctrl+n"):
            if not keyboard.wait(hotkey="ctrl+c"):
                # 这个ctrl+c 复制图片需要时间，所以要让程序停会。
                time.sleep(0.1)  # 单位秒,0.01秒
                image = ImageGrab.grabclipboard()
                image.save('test.png')
                # 如果报错 image没有save方法，很可能是image不是图片内容，或者说很可能空

    def reg(self):
        from aip import AipOcr
        client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        # 使用百度云的产品 人工智能-文字识别 接口
        """ 读取图片 """

        with open(self.FILEPATH, 'rb') as fp:
            image = fp.read()

        """ 调用通用文字识别, 图片参数为本地图片 """
        # client.basicGeneral(image);

        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        result = client.basicGeneral(image, options)
        all_text = ''
        for i in result['words_result']:
            all_text += i['words'] + '\n'
            # all_text += '\n'
        # print(all_text)
        return all_text


def main():
    r = RecGt()
    r.screeshot()
    txt = r.reg()
    print(txt)


if __name__ == '__main__':
    main()
