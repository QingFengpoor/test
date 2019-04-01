#Scipy实际应用
#1、查看实时票房
import tushare as ts
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
import numpy as np
import csv

# 获取单日票房排行数据
day =ts.realtime_boxoffice()
print(day)

# 查看某日的票房
day1 = ts.day_boxoffice('2018-05-26')
print(day1)

#2、股票简单分析

# 获取这个时间段的股票交易信息，
all = ts.get_h_data('600848',start='2018-10-24',end='2019-02-27')

#从股票数据集中获取时间作为x轴
x = all.index
print(x)

# 从股票数据集中获取收盘价作为y轴
y =  all['close']
print(y)

#用detrend函数去除数据样本线性趋势
trend = signal.detrend(y)

#利用得到的x和y进行绘图
plt.plot(x,y,"g",x,y-trend,"-")
plt.show()

#3、每天获取新闻简要，并写入到文件中

new = ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
data = np.array(new)
out = open('data/new.csv','a',newline='')
writer = csv.writer(out,dialect="excel")
for i in range(len(data)):
    writer.writerow(data[i])
print("写入成功！")
out.close()

