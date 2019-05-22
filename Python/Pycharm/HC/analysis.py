from fromwebHC import webHC

import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram

import pandas as pd

import numpy as np

if __name__=="__main__":

    path="C:/Users/feng/Documents/AI/1030416121 朱青峰  实验六/"

    linkagemethed=["single","complete","average"]

    dataset = pd.read_csv('data.txt',sep=' ')

    lm=plt.figure("linkagemethed",(8,8))

    for i in range(len(linkagemethed)):

        result,ccenter,row_clusters,labels=webHC(dataset,4,linkagemethed=linkagemethed[i])

        plt.subplot(3,2,2*i+1)

        plt.title(linkagemethed[i])

        plt.scatter(dataset.iloc[:,0].values,dataset.iloc[:,1],c=result)

        plt.subplot(3,2,2*i+2)

        row_dendr = dendrogram(row_clusters,labels=labels)

        plt.tight_layout()

        plt.ylabel("euclidean dist")

    plt.savefig(path+"linkagemethed.png")

    #plt.show()

    inertiaarray=np.ndarray(10)

    for i in range(1,11,1):

        result,ccenter,row_clusters,labels=webHC(dataset,i,linkagemethed=linkagemethed[1])

        for j in range(i):

            inertiaarray[i-1]+=sum(np.sqrt(np.sum(np.asarray(ccenter[j]-dataset.iloc[np.nonzero(result==j+1)].values)**2,axis=1)))

    #print(inertiaarray)

    plt.figure("inerti")

    plt.title("inerti 1-10")

    plt.scatter(range(1,11),inertiaarray,c="r",marker="o")

    textdic={"family":"Times New Roman","color":"yellow","weight":'normal',"size":12}

    for i in range(1,11):

        plt.text(i,inertiaarray[i-1]+14,str(round(inertiaarray[i-1],2)),fontdict=textdic)

    plt.plot(range(1,11),inertiaarray,c="b")

    plt.xlim((0,11))

    plt.ylim(0.5*min(inertiaarray),1.2*max(inertiaarray))

    plt.savefig(path+"inerti.png")

    plt.show()
