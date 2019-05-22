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
