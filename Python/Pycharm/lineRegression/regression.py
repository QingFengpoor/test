import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('Salary_data.csv')
X=dataset.iloc[:,0].values
Y=dataset.iloc[:,-1].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
X_train=X_train.reshape(-1,1)
Y_train=Y_train.reshape(-1,1)

regresor=LinearRegression()
regresor.fit(X_train,Y_train)
predict=regresor.predict(X_train.reshape(-1,1))


k=regresor.coef_
b=regresor.intercept_
t1=np.zeros_like(X_train)
t2=np.zeros_like(X_test)
YTe=np.zeros_like(X_test)

for i in range(len(X_test)):
    YTe[i]=k*X_test[i]+b

for i in range(len(predict)):
    t1[i][-1]=sp.sqrt((predict[i][-1]-Y_train[i][-1])**2)
for i in range(len(Y_test)):
    t2[i]=sp.sqrt((YTe[i]-Y_test[i])**2)
print("训练集均方差：",mean_squared_error(Y_train,predict))
print("测试集均方差：",mean_squared_error(Y_test.reshape(-1,1),YTe.reshape(-1,1)))

plt.figure(figsize=(14,14))

figure=plt.subplot(211)
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,predict,color='black')
plt.scatter(X_train, t1, color='pink')
plt.legend(['linear','origin data','offset'])#优先表示plot作图
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Train set')

plt.subplot(212)
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,predict,color='black')
plt.scatter(X_test, t2, color='pink')
plt.legend(['origin data','liner','offset'])
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Test set')
plt.show()


