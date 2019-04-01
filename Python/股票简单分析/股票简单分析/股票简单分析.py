import tushare as ts
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# 获取这个时间段的股票交易信息，
all = ts.get_h_data('600848',start='2018-10-24',end='2019-03-03')

#从股票数据集中获取时间作为x轴
x = all.index
print(x)

# 从股票数据集中获取收盘价作为y轴
y =all['close']
print(y)

#用detrend函数去除数据样本线性趋势
trend = signal.detrend(y)

#利用得到的x和y进行绘图
plt.plot(x,y,"g",x,y-trend,"-")
plt.show()

