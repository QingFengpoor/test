import urllib.request
#下载图片
image_url='http://k.zol-img.com.cn/sjbbs/7692/a7691515_s.jpg'
response=urllib.request.urlopen(image_url)
#方式一 用二进制的方式写入文件
#with open('bizhi.jpg','wb') as fp:
#    fp.write(response.read())

#方式二 用urllib.request.urlretrieve(url,image_path)函数
urllib.request.urlretrieve(image_url,'bizhi2.jpg')