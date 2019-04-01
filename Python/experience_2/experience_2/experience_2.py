from scipy import stats as st
from matplotlib import pyplot as plt
import numpy as np

population_ages = [22,55,62,45,21,22,34,42,42,4,99,28,35,30,25,27,49,111,37,44,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#绘图
plt.hist(population_ages,bins)
#显示指令
plt.show()

# 正太分布
normalExample = st.norm.rvs(size=100)

# # 计算正太分布样本点的偏度和数据样本与正太分布拟合程度
skew, pvalue = st.skewtest(normalExample)
# 偏度skew大于0则是正偏，否则是负偏
print("偏度", skew)

#绘制数据样本的直方图
plt.figure(figsize=(10,5))
plt.plot(normalExample)
plt.fill_between(skew, pvalue, 10, color = 'green')
plt.show()

# 计算均值
average = np.mean(normalExample)
print(average)

# 计算峰度
kurtosistest,pvalue= st.kurtosistest(normalExample)

# 峰度的正负
print(kurtosistest)

# 找到位于95%位置的数据点
reuslt = st.scoreatpercentile(normalExample, 95)
print(normalExample)
# 在所有的数据样本中比result小的数据展95%，比result值大的数据样本点占5%
print('95%', reuslt)

# 求给定的一个数值在数据样本中的百分比位置
percent = st.percentileofscore(normalExample,0.8)
normalExample.sort()
print(normalExample)
print("0.8在样本中的位置",percent)

