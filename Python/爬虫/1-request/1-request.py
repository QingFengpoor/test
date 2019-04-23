import urllib.request

url='http://www.baidu.com'
response=urllib.request.urlopen(url=url)
print(response)
#print(response.read().decode()) read的内容只能读一遍 读完就空了 读的内容是字节型的
#print(response.geturl()) geturl()通过响应信息获得请求头
#print(response.getheaders())  getheaders()返回的内容是一个列表 每个元组是一个键值对 通过以下方法改为字典类型
#print(dict(response.getheaders())) 转为字典类型
#print(response.getcode()) 返回状态码
#print(response.readlines())返回列表，按行读取，都是字节类型


#以UTF-8格式写
with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.read().decode())

#以二进制内容往里写
with open('baidu.html','wb') as fp:
    fp.write(response.read())

