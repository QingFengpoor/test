#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:58:14 2019

@author: yang
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix,classification_report #对结果的衡量
from sklearn.preprocessing import LabelBinarizer                   #将[0,9]转化为如果是为1，不是就为0的样子
from NeuralNetwork import NeuralNetwork
from sklearn.model_selection import train_test_split               #划分训练集与测试集

digits=load_digits()
X=digits.data
Y=digits.target
X-=X.min()
X/=X.max()

nn=NeuralNetwork([64,100,10])
X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
labels_train = LabelBinarizer().fit_transform(Y_train)
labels_test = LabelBinarizer().fit_transform(Y_test)
print(X_train.shape)
print(labels_train.shape)
print("start fitting")
nn.fit(X_train,labels_train,epochs=3000)
prdictions=[]
for i in range(X_test.shape[0]):
    #print(X_test[i])
    o=nn.predict(X_test[i])
    prdictions.append(np.argmax(o))  #最大的概率对应的那个数
print(Y_test)
print(prdictions)
#print(Y_test,prdictions)
print(confusion_matrix(Y_test,prdictions))
print(classification_report(Y_test,prdictions))
