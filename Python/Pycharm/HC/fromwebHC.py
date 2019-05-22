
import pandas as pd

from numpy import *

from scipy.spatial.distance import pdist,squareform

from scipy.cluster.hierarchy import dendrogram

import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import fcluster

def webHC(dataset,k,metric="euclidean",linkagemethed="complete"):

    variables=dataset.columns.values

    labels=list(range(shape(dataset)[0]))

    labels=["s"+str(x) for x in labels]

    dist_matrix=pd.DataFrame(squareform(pdist(dataset,metric=metric)),columns=labels,index=labels)

    #print(dist_matrix)

    from scipy.cluster.hierarchy import linkage

    #以全连接作为距离判断标准，获取一个关联矩阵

    row_clusters = linkage(dist_matrix.values,method=linkagemethed,metric=metric)

    #print(row_clusters)

    '''
    
    #将关联矩阵转换成为一个DataFrame

    clusters = pd.DataFrame(row_clusters,columns=["label 1","label 2","distance","sample size"],

                            index=["cluster %d"%(i+1) for i in range(row_clusters.shape[0])])

    print(clusters)
    
    '''

    result=fcluster(row_clusters,criterion="maxclust",t=k)

    #print(result)

    ccenter=ndarray((k,2))

    for i in range(k):
        ccenter[i]=mean(dataset.iloc[nonzero(result==i+1)].values,axis=0)

    #print(ccenter)

    return result,ccenter,row_clusters,labels

if __name__ == "__main__":

    dataset = pd.read_csv('data.txt',sep=' ')

    result,ccenter,row_clusters,labels=webHC(dataset,4,metric="euclidean",linkagemethed="complete")

    plt.figure("scatter")

    plt.scatter(dataset.iloc[:,0].values,dataset.iloc[:,1],c=result)

    plt.figure("dendrogram")

    row_dendr = dendrogram(row_clusters,labels=labels)

    plt.tight_layout()

    plt.ylabel("euclidean dist")

    plt.show()
