#!/usr/bin/python
# coding=utf-8
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
import time
dataset = pd.read_csv('data.txt',sep=' ')
X = dataset.iloc[:,0].values
Y = dataset.iloc[:,1].values
Z = dataset.iloc[:,:].values
plt.figure(1,figsize=(8,5)) #设置画布大小
plt.scatter(X,Y,color='blue')
# 加载数据
def loadDataSet(fileName): # 解析文件，按 tab 分割字段，得到一个浮点数字类型的矩阵
    dataMat = [] # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine) # 将每个元素转成 float 类型
        dataMat.append(fltLine)
    return dataMat
# 计算欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) # 求两个向量之间的距离
#改进初始质点 先选择一个随机点 然后选择与前面的点最远的点为接下来的那个质点
def betterrandCent(dataSet,k):
    n=shape(dataSet)[1]
    m=shape(dataSet)[0]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[0,j] = minJ + rangeJ * random.rand(1, 1)
    for i in range(len(centroids)-1):
        Temp=mat(zeros((m,1)))
        for j in range(len(dataSet)):
            t=0
            for c in range(i+1):
                if((dataSet[j]==centroids[c]).all()):break
                t+=distEclud(dataSet[j],centroids[i])
            Temp[j]=t
        mx=max(Temp)
        ptsInClust = dataSet[nonzero(Temp[:,0].A == mx)[0]]
        centroids[i+1]=ptsInClust
    return  centroids
# 构建聚簇中心，取 k 个(此例中为 4)随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n))) # 每个质心有 n 个坐标值，总共要 k 个质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
        for i in range(k-1):
            if((centroids[i]==centroids[k-1]).all()):j=j-1
    print("centroids",k)
    print(centroids)
    return centroids


# k-means 聚类算法
def kMeans(dataSet, k, i,distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2))) # 用于存放该样本属于哪类及质心距离
    # clusterAssment 第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    if(i==0):
        centroids=betterrandCent(dataSet,k)
    else:
        centroids = createCent(dataSet, k)
    clusterChanged = True # 用来判断聚类是否已经收敛
    while clusterChanged:
        clusterChanged = False;
        for i in range(m): # 把每一个数据点划分到离它最近的中心点
            minDist = inf; #inf 表示无穷大
            minIndex = -1;#初始默认质点不存在
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j # 如果第i个数据点到第j个中心点更近，则将 i 归属为 j
            if clusterAssment[i,0] != minIndex: clusterChanged = True; # 如果分配发生变化，则需要继续迭代
            clusterAssment[i,:] = minIndex,minDist**2 # 并将第 i 个数据点的分配情况存入字典
        for cent in range(k): # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]] # 去第一列等于 cent 的所有列
            centroids[cent,:] = mean(ptsInClust, axis = 0) # 算出这些数据的中心点
    return centroids, clusterAssment
# --------------------测试----------------------------------------------------
# 用测试数据及测试 kmeans 算法
color='rgbycmykw'
#dataMat = mat(loadDataSet('testSet.txt'))
plt.figure(2,figsize=(8,5))
dataMat=Z

K=int(input("input k:"))
myCentroids1, clustAssing = kMeans(dataMat, K,1)
plt.subplot(1,2,1)#第一张:myCentroids
for i in range(len(myCentroids1)):
    plt.plot(myCentroids1[i,0],myCentroids1[i,1],"ro",color=color[i])
plt.title("随机初始",{'family':'SimHei','size':6})

plt.subplot(1,2,2)#第二张：dataMat 聚类结果染色图
for i in range(len(dataMat)):
    plt.plot(dataMat[i,0],dataMat[i,1],"ro",color=color[int(clustAssing[i,0])])
llfc=[]
for i in range(K):
    ptsInClust=clustAssing[nonzero(clustAssing[:,0].A==i)[0]]
    llfc.append(round(sum(sqrt(ptsInClust[:,1])),2))
plt.legend(llfc,loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.,prop={'family':'SimHei','size':6})


plt.figure(3,figsize=(8,5))
myCentroids0, clustAssing = kMeans(dataMat, K,0)
plt.subplot(1,2,1)#第一张:myCentroids
for i in range(len(myCentroids0)):
    plt.plot(myCentroids0[i,0],myCentroids0[i,1],"ro",color=color[i])
plt.title("选择最远",{'family':'SimHei','size':6})

plt.subplot(1,2,2)#第二张：dataMat 聚类结果染色图
for i in range(len(dataMat)):
    plt.plot(dataMat[i,0],dataMat[i,1],"ro",color=color[int(clustAssing[i,0])])
llfc=[]
for i in range(K):
    ptsInClust=clustAssing[nonzero(clustAssing[:,0].A==i)[0]]
    llfc.append(round(sum(sqrt(ptsInClust[:,1])),2))
plt.legend(llfc,loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.,prop={'family':'SimHei','size':6})

#print("myCentroids0:")
#print(myCentroids0)
#print("myCentroids1:")
#print(myCentroids1)
plt.figure(4)
Yllfc=[]
D=15#测试组数
for i in range(2,D):
    myCentroids1, clustAssing = kMeans(dataMat, i,1)
    print("myCentroids",i)
    print(myCentroids1)
    llfc=[]
    for j in range(0,i):
        ptsInClust=clustAssing[nonzero(clustAssing[:,0].A==j)[0]]
        llfc.append(round(sum(sqrt(ptsInClust[:,1])),2))
    Yllfc.append(mean(llfc))
for i in range(0,D-3):
    Yllfc[i]=Yllfc[i]-Yllfc[i+1]
plt.plot(range(2,D-1),Yllfc[0:D-3],color='r')
plt.scatter(range(2,D-1),Yllfc[0:D-3],color='b')
plt.show()
