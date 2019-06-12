#可用资源
Available=[]
#最大需要的资源数
maxNeed=[]
#已有的资源
Allocated=[]
#需要的资源数
Need=[]
# 最大5个线程
Finsh=[False,False,False,False,False]
#剩余资源
Free=[]
#输出最终序列
seq=[]
#初始化可用资源
Available.append(1)
Available.append(0)
Available.append(2)
Available.append(0)
#赋值给剩余资源
Free=Available
#初始化最大需要的资源数
maxNeed.append([4,1,1,1])
maxNeed.append([0,2,1,2])
maxNeed.append([4,2,1,0])
maxNeed.append([1,1,2,1])
maxNeed.append([2,1,1,0])
#初始化已有的资源
Allocated.append([3,0,1,1])
Allocated.append([0,1,0,0])
Allocated.append([1,1,1,0])
Allocated.append([1,1,0,1])
Allocated.append([0,0,0,0])

#初始化需要的资源数，需要的资源数=最大资源数-已有的资源数
for i in range(0,len(Finsh)):
    needList=[]
    m=maxNeed[i]
    a=Allocated[i]
    for j in range(0,len(Available)):
        needList.append(m[j]-a[j])
    Need.append(needList)

#是否能够分配完成
def isFinsh(f):
    for i in f:
        if f[i]==False:
            return False
    return True

#校验剩余的资源是否够分给给need对应的进程
def check(need,free):
    for i in range(0,len(free)):
        flag = True;
        if  free[i]>=need[i]:
            pass
        else:
            return False
    return flag
#校验没问题了，才会分配（省略分配，直接回收）并且回收
def addFree(allocated,free):
    for i in range(0,len(free)):
        free[i]=allocated[i]+free[i]
#循环终止条件是找到可以安全分配的序列，如果找不到会一直死循环。。可以采取其它措施，但是这里就不写了
while True:
    if not isFinsh(Finsh):
        for i in range(0,len(Finsh)): #循环所有的请求线程
           if not Finsh[i]:   # 如果这个线程没有完成
               if check(Need[i],Free):
                   addFree(Allocated[i],Free)
                   Finsh[i]=True;
                   print(Finsh)
                   print(Free)
                   seq.append(i+1);
           else:
               continue
    else:
        break


print(seq)
