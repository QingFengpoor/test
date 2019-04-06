import requests
import os
url="http://img0.dili360.com/ga/M00/47/EF/wKgBzFlDQnWAU5dKACd7TLyocKo220.tub.jpg@!rw9"
root=os.getcwd()
path=root+'\\'+url.split('/')[-1].split('@')[-2]
print(path)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        try:
            r=requests.get(url)
            r.raise_for_status()
            with open(path,'wb')as f:
                f.write(r.content)
                f.close()
            print('文件保存成功')
        except:
            print('连接失败')
        
    else:
        print('文件已存在')
except:
    print("爬取失败")
