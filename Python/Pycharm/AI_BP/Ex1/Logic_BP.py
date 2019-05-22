#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:44:42 2019

@author: yang
"""

from NeuralNetwork import NeuralNetwork#导入刚才写的对象
import numpy as np

nn=NeuralNetwork([2,2,1],'tanh')

X = np.array([[0,0],[0,1],[1,0],[1,1]])
print("X:",X)
Y = np.array([0,1,1,0])    #也就是或运算嘛
print("Y:",Y)
nn.fit(X,Y)
#print("nn:",nn)
for i in [[0,0],[0,1],[1,0],[1,1]]:
    print(i,nn.predict(i))