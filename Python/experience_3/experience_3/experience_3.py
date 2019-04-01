import numpy as np
from scipy import stats,linalg
#1检测数据样本和正太分布的拟合程度
normalExample = stats.norm.rvs(size=100)
skew, pvalue1 = stats.skewtest(normalExample)
print("pvlaue-1:", pvalue1)
#2线性代数的应用
#创建一个测试数组,注意矩阵才能求逆，要定义mat
testArr = np.mat(np.array([[2,4],
                    [4,7]]))

# 用scipy 计算行列式
result = linalg.det(testArr)
print("矩阵的行列式为：",result)

# 用scipy求矩阵的逆
testArr_ = linalg.inv(testArr)
print("矩阵的逆矩阵为：",testArr_)
# 验证
testArr*testArr_

# 奇异值分解
U,sigma,V = linalg.svd(testArr)
print("U: \n",U)
print("sigma:",sigma)
print("V: \n",V)

# scipy解方程组
'''
x - 2y + z = 0
2y - 8z = 8
-4x + 5y + 9z = ?9
'''
A = np.mat("1 -2 1;0 2 -8; -4 5 9")
B = np.array([0,8,-9])
x = linalg.solve(A,B)
print("x ={},y={},z={}".format(x[0],x[1],x[2]))
