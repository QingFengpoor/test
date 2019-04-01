import requests
url="http://www.baidu.com/s"
keyword="python"
try:
    kv={'wd':keyword}
    r=requests.get(url,params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
