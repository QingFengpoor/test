import urllib.parse

#把参数拼接到url里
url='http://www.baidu.com'
#参数有 name age sex height
#拼接后的结果为 url='http://www.baidu.com?name=goudan&age=18&sex='nv'&height=180'
name='goudan'
age=18
sex='nv'
height='180'

#构建一个字典
data={
    'name':name,
    'age':age,
    'sex':sex,
    'height':height,
}
#遍历字典并把k='v'放到列表里
lt=[]
for k,v in data.items():
    lt.append(k+'='+str(v))
#使用&拼接列表的每个元组 结果为query_string
query_string1='&'.join(lt);
#把参数拼接道url
url1=url+'?'+query_string1

print(url1);

#以上query_string的形成可以通过urlencode（字典) 产生 同时encode会对内容url编码
query_string2=urllib.parse.urlencode(data)
url2=url+'?'+query_string2
print(url2)
