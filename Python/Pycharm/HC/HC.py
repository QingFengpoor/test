import pandas as pd
from numpy import *
from math import *
import matplotlib.pyplot as plt
dataset = pd.read_csv('data.txt',sep=' ')
X = dataset.iloc[:,0].values
Y = dataset.iloc[:,1].values
Z = dataset.iloc[:,:].values
plt.figure(figsize=(8,5)) #设置画布大小
plt.scatter(X,Y,color='blue')

#Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering
num_clusters = 4
hc_cluster = AgglomerativeClustering(n_clusters=num_clusters, linkage='ward')

def calculateAB(A,B):
    return sqrt(sum(power(A - B, 2)))
def HC(dataset,k,calculate=calculateAB):
    dataset=dataset.values
    m=shape(dataset)[0]
    ck=m
    clumap=zeros((m,1))#m行1列 表示点属于的类别
    for i in range(m):
        clumap[i,0]=i
    centrodis=dataset#centrodis表示每个类的中心点
    while(ck>k):
        distmap=zeros((ck,ck))#ck 行 ck 列的矩阵 存储相应的两个类之间的距离
        for i in range(ck):
            for j in range(i,ck):
                distmap[i,j]=calculate(centrodis[i,:],centrodis[j,:])
        tck=ck
        fl=int(ck%2)#判断当前已完成是不奇数个类
        if fl==1:
            print("这时 有奇数个类要合并")
        ck=ceil(ck/2.0)
        tcentrodis=centrodis
        centrodis=zeros((ck,2))
        s=0
        tL=[]
        for i in range(tck-1):#依次找每一类的最小邻近类
            #当前类已经合并过了
            if i in tL:
                continue
            #找到要合并的两个类
            mJ=distmap[i][i+1]
            mj=i+1
            for j in range(i+1,len(distmap)):
                if(distmap[i][j]<mJ and j not in tL ):
                    mJ=distmap[i][j]
                    mj=j
            if (mj not in tL and i not in tL) :
                tL.append(mj)
                tL.append(i)
                #进行合并
                #更新类中心
                print("s:",s)
                print("tL:",tL)
                centrodis[s,0]=(tcentrodis[i,0]+tcentrodis[mj,0])/2
                centrodis[s,1]=(tcentrodis[i,1]+tcentrodis[mj,1])/2
                #标记合并的两个点
                for a in range(len(clumap)):
                    if clumap[a,0]==i:
                        clumap[a,0]=s
                for b in range(len(clumap)):
                    if clumap[b,0]==mj:
                        clumap[b,0]=s
                s=s+1
            elif fl==1:#奇数类时单处理
                tL.append(i)
                #进行合并
                #更新类中心
                print("s:",s)
                print("tL:",tL)
                #中心点不变
                centrodis[s]=tcentrodis[i]
                #更新点所属的类
                for a in range(len(clumap)):
                    if clumap[a,0]==i:
                        clumap[a,0]=s
                s=s+1
            else:
                print("mj=",mj,"\t i=",i)
                print(tL)
                print("not in tL is wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
        for j in range(ck):
            print("类",j,":")
            tj=[]
            for h in range(len(clumap)):
                if clumap[h][0]==j:
                    tj.append(h)
            print(tj)
        for j in range(len(tL)):
            if j not in tL:
                print(j)
                print("有遗漏!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("HC:",centrodis)








HC(dataset,2)
#返回各自文本的所被分配到的类索引
result = hc_cluster.fit_predict(Z)
print ("Predicting result: ", result)
plt.figure(figsize=(8,5)) #设置画布大小#绘制散点图 参数：x横轴 y纵轴 c=y_pred聚类预测结果 marker类型 o表示圆点 *表示星型 x表示点
plt.scatter(X, Y, c=result, marker='o')
 
#绘制标题
plt.title("HC Data")
#绘制x轴和y轴坐标
plt.xlabel("X")
plt.ylabel("Y")
#设置右上角图例
#plt.legend(["A","B","C"])
 
#显示图形
plt.show()
