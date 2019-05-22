import pandas as pd
from numpy import *
from math import *
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.txt',sep=' ')
plt.figure(figsize=(8,5)) #设置画布大小
plt.scatter(dataset.iloc[:,0].values,dataset.iloc[:,1].values,c='blue')#原始点
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
        ck=ceil(ck/2.0)#理想情况下 每次都折半
        if ck<k:#当折半后ck小于了k
            ck=k
        f2=tck-ck#需要合并的次数
        tcentrodis=centrodis
        centrodis=zeros((tck,2))
        s=0
        tL=[]
        for i in range(tck-1):
            #依次找除最后一个类的每一类的最小邻近类
            #当前类已经合并过了
            if i in tL:
                continue
            #找到要合并的两个类
            mJ=distmap[i][i+1]
            mj=i+1
            f1=0#标记谁否合并了最后一个类
            for j in range(i+1,len(distmap)):
                if(distmap[i][j]<mJ and j not in tL ):
                    #这时候在纵向比较一下确认是不是最小
                    if distmap[i,j]!=min(distmap[i:j-1,j]):#在纵向比较的时候 ， 发现并不是最小的那个 就继续找
                        continue#碰到了 没有匹配项的情况 其实并不应该折半 这时候就单独把他做一个类
                    mJ=distmap[i][j]
                    mj=j
            if (mj not in tL and i not in tL and s<f2) :
                if mj == tck-1:
                    f1==1 #合并了最后一个类
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
            elif s>=f2:#不需要合并时
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
                print("这时就单独做个类")
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
            if i==tck-2 and s > f2 and f1==0:#当循环到最后倒数第二个类 且最后一个类没有被合并 要被单独成一个类时
                print("单处处理最后一个类***********************************************")
                print("这时就单独做个类")
                tL.append(i+1)
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
        ck=s
        tcentrodis=zeros((s+1,2))
        tcentrodis[:,:]=centrodis[0:s+1,:]
        for j in range(s):
            print("类",j,":")
            tj=[]
            for h in range(len(clumap)):
                if clumap[h][0]==j:
                    tj.append(h)
            print(tj)
        print("ck=",ck)
        for j in range(len(tL)):
            if j not in tL:
                print(j)
                print("有遗漏!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("HC:",centrodis)
    for j in range(ck):
        print("类",j,":")
        tj=[]
        for h in range(len(clumap)):
            if clumap[h][0]==j:
                tj.append(h)
        print(tj)
    print("ck=",ck)
    return centrodis,clumap

def my_plot(dataset,clumap):
    plt.figure("fmy_plot")
    plt.title("my_HC")
    X=dataset.iloc[:,0].values
    Y=dataset.iloc[:,1].values
    k=int(max(clumap[:,0]))+1#分类的类数
    print("my_plot k=:",k)
    if k>7:
        print("类的数目过多 不能用不同颜色")
        return
    sc="brygckm"
    for i in range(k):
        x=[]
        y=[]
        for j in range(len(clumap)):
            if clumap[j,0]==i:
                x.append(X[j])
                y.append(Y[j])
        plt.scatter(x,y,c=sc[i])

def usingac(dataset):
    X = dataset.iloc[:,0].values
    Y = dataset.iloc[:,1].values
    Z = dataset.iloc[:,:].values
    #Hierarchical Clustering
    from sklearn.cluster import AgglomerativeClustering
    num_clusters = 4
    hc_cluster = AgglomerativeClustering(n_clusters=num_clusters, linkage='ward')
    result = hc_cluster.fit_predict(Z)
    print ("Predicting result: ", result)
    plt.figure(figsize=(8,5)) #设置画布大小#绘制散点图 参数：x横轴 y纵轴 c=y_pred聚类预测结果 marker类型 o表示圆点 *表示星型 x表示点
    plt.scatter(X, Y, c=result, marker='o')

    #绘制标题
    plt.title("HC Data")
    #绘制x轴和y轴坐标
    plt.xlabel("X")
    plt.ylabel("Y")


centrodis,clumap=HC(dataset,4)
print("clumap:\n",clumap)
my_plot(dataset,clumap)

usingac(dataset)
plt.show()
