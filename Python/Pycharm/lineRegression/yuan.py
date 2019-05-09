import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0].values
Y = dataset.iloc[:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
X_train = X_train.reshape(-1, 1)
Y_train = Y_train.reshape(-1, 1)

regresor = LinearRegression()
regresor.fit(X_train, Y_train)

predict = regresor.predict(X_train.reshape(-1, 1))

plt.figure(figsize=(10, 12))
figure = plt.subplot(211)

plt.scatter(X_train, Y_train, color='red', label='train')
plt.scatter(X_train, abs(Y_train-predict), color='blue', label='error')
plt.plot(X_train, predict, color='black', label='best line')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Train set')
plt.legend(['best line', 'train', 'error'])

plt.subplot(212)
predict1 = regresor.predict(X_test.reshape(-1, 1))

plt.plot(X_train, predict, color='black', label='best line')
plt.scatter(X_test.reshape(9, ), abs(Y_test-predict1.reshape(9, )), color='blue', label='error')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Test set')
plt.legend(['best line', 'train', 'error'])
plt.show()

