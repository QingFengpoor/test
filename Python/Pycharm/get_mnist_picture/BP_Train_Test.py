#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:10:03 2019

@author: yang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:18:40 2019

@author: yang
"""
from BP import BP#导入刚才写的对象
import numpy as np
import matplotlib.pyplot as plt
import cv2
N = 6
X_data=[]
for i in range(N):
    img=cv2.imread("MNIST_data/train/mnist_train_%d.jpg"%i)
    r,g,b=[img[:,:,i] for i in range(3)]
    img_gray=r*0.299+g*0.587+b*0.114
    img_gray_1D=img_gray.flatten()
    X_data.append(img_gray_1D)
X_data = np.array(X_data)
#X_data = np.transpose([X_data])
#y_data = np.exp(-X_data) * np.sin(2 * X_data)
y_data=[]
with open('MNIST_data/mnist_train_label.txt','r') as f:
    for i in range(N):
        y_data.append(float(f.readline().strip()))
y_data=np.array(y_data)
print(y_data)
#y_data=2*np.sin(X_data)-0.7
bp = BP(n_hidden=3,f_output='linear', maxstep=4000, eta=0.01, alpha=0.1)  # 注意学习率若过大，将导致不能收敛
print(X_data.shape,y_data.shape)
bp.fit(X_data, y_data)
#plt.figure(1)
#plt.subplot(121)
#plt.plot(X_data, y_data)
pred = bp.predict(X_data)
print(pred)
#plt.scatter(X_data, pred, color='r')
plt.show()

