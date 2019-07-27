# coding=utf-8

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16898200'
API_KEY = 'EvSWmvXiNoRt3mW2s7ox8KYi'
SECRET_KEY = 'INx9wooqlHnrwRg8vkvQq8MF7y7BH4UG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('test.png')

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
    all_text += i['words']+'\n'
    # all_text += '\n'
print(all_text)