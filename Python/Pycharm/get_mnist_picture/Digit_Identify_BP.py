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
import cv2
import math
import matplotlib.pyplot as plt

N = 60000
X_train=[]
for i in range(N):
    img=cv2.imread("MNIST_data/train/mnist_train_%d.jpg"%i)
    r,g,b=[img[:,:,i] for i in range(3)]
    img_gray=r*0.299+g*0.587+b*0.114
    img_gray_1D=img_gray.flatten()
    #for i in range(len(img_gray_1D)):
    #    if img_gray_1D[i]<127:
    #        img_gray_1D[i]=0
    #    else:
    #        img_gray_1D[i]=1
    #img_gray_1D-=img_gray_1D.min()
    #img_gray_1D/=img_gray_1D.max()
    img_gray_1D=img_gray_1D/255.0
    X_train.append(img_gray_1D)
X_train = np.array(X_train)
#X_data = np.transpose([X_data])
#y_data = np.exp(-X_data) * np.sin(2 * X_data)
Y_train=np.zeros((N,10))
Y_label=[]
with open('MNIST_data/mnist_train_label.txt','r') as f:
    for i in range(N):
        Y_label.append((int(float(f.readline().strip()))))
        Y_train[i]=0
        Y_train[i][(int(float(f.readline().strip())))]=1
#Y_train=np.array(Y_train)
print(Y_train)
print(Y_label)
nn=NeuralNetwork([X_train.shape[1],3*X_train.shape[1],10],activation='logistic')#int(math.sqrt(X_train.shape[1]+10))+10 #3 5   activation='tanh'
#X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
#labels_train = LabelBinarizer().fit_transform(Y_train)
#labels_test = LabelBinarizer().fit_transform(Y_test)
print("start fitting")
nn.fit(X_train,Y_train,epochs=3000)
prdictions=[]
for i in range(X_train.shape[0]):
    #print(X_test[i])
    o=nn.predict(X_train[i])
    prdictions.append(np.argmax(o))  #最大的概率对应的那个数
print(prdictions)
count=0
for i in range(len(prdictions)):
    if prdictions[i]==Y_label[i]:
        count+=1
rate=count/len(prdictions)
print(rate)
#plt.plot(range(N),Y_label,c="b")
plt.plot(range(N),np.abs(np.array(Y_label)-np.array(prdictions)),c="r")
plt.xlim([-10,N+10])
plt.show()
#print(confusion_matrix(Y_test,prdictions))
#print(classification_report(Y_test,prdictions))
