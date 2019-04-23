import urllib.parse

image_url='http://pic1.win4000.com/wallpaper/9/5450ae2fdef8a.jpg'

#url只能由特定的字符组成 字母，数字，下划线
#如果出现其他的 比如 $ 空格 中文等，就要对其编码

url='https://www.baidu.com/baidu?wd=中文&tn=monline_4_dg&ie=utf-8'
encode_url=urllib.parse.quote(url);#对url 进行编码 主要是对中文
decode_url=urllib.parse.unquote(url);#对url 进行解码 主要是对中文 
print(encode_url);
print(decode_url);