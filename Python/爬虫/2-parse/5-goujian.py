#构建请求头信息(反爬虫第一步)
import urllib.request
import urllib.parse

url='http://www.baidu.com/'

#response=urllib.request.urlopen(url)

#print(response.read().decode())

#伪装请求头UA

#定制头部
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
}
#构建请求对象
requestre=urllib.request.Request(url=url,headers=headers)
#发送请求
responsere=urllib.request.urlopen(requestre)
print(responsere.getcode())
#print(responsere.read().decode())
