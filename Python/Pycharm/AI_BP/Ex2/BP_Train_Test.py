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
N = 100
X_data = np.linspace(1, 1.6, N)
X_data = np.transpose([X_data])
#y_data = np.exp(-X_data) * np.sin(2 * X_data)
y_data=2*np.sin(X_data)-0.7
bp = BP(n_hidden=3,f_output='linear', maxstep=10000, eta=0.01, alpha=0.1)  # 注意学习率若过大，将导致不能收敛
bp.fit(X_data, y_data)
plt.figure(1)
plt.subplot(121)
plt.plot(X_data, y_data)
pred = bp.predict(X_data)
plt.scatter(X_data, pred, color='r')
x1=np.sum(np.power(np.round(pred-y_data,4),2))

bp=None
pred=None
bp = BP(n_hidden=7,f_output='linear', maxstep=60000, eta=0.01, alpha=0.1)  # 注意学习率若过大，将导致不能收敛
bp.fit(X_data, y_data)
pred = bp.predict(X_data)
plt.subplot(122)
plt.plot(X_data, y_data)
plt.scatter(X_data, pred, color='r')
x2=np.sum(np.power(np.round(pred-y_data,4),2))
print(x1,x2)
'''
plt.figure(2)
wucha=[]
start=5000
stop=65000
step=5000
for i in range(start,stop,step):
    bp=None
    pred=None
    bp = BP(n_hidden=3,f_output='linear', maxstep=i, eta=0.01, alpha=0.1)  # 注意学习率若过大，将导致不能收敛
    bp.fit(X_data, y_data)
    pred = bp.predict(X_data)
    wucha.append(np.sum(np.power(np.round((pred-y_data),4),2)))
print(wucha)
plt.subplot(121)
plt.plot(range(start,stop,step),wucha,c="b")
plt.scatter(range(start,stop,step),wucha,c="r")
plt.subplot(122)
plt.scatter(X_data,y_data,c="b")'''
plt.show()

