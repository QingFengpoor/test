import queue
import math
import copy
import numpy as np
import matplotlib.pyplot as plt


class clusterNode:
	def __init__(self, value, id=[],left=None, right=None, distance=-1,  count=-1, check = 0):
		'''
		value: 该节点的数值，合并节点时等于原来节点值的平均值
		id：节点的id，包含该节点下的所有单个元素
		left和right：合并得到该节点的两个子节点
		distance：两个子节点的距离
		count：该节点所包含的单个元素个数
		check：标识符，用于遍历时记录该节点是否被遍历过
		'''
		self.value = value
		self.id = id
		self.left = left
		self.right = right
		self.distance = distance
		self.count = count
		self.check = check

	def show(self):
		#显示节点相关属性
		print(self.value,' ',self.left.id if self.left!=None else None,' ',\
			self.right.id if self.right!=None else None,' ',self.distance,' ',self.count)

	def showall(self):
		print(self.value,' ',self.id,self.left,self.right,self.distance,self.count,self.check)

class hcluster:

	def distance(self,x,y,dataset,method):

		#计算两个节点的距离，可以换成别的距离
		if method=="single":
			dis=1000
			for i in dataset:
				if i.id[0] in x.id:
					tdis=0
					for j in dataset:
						if j.id[0] in y.id:
							tdis=round(np.sqrt(np.sum(np.power((i.value-j.value),2),axis=0)),2)
							if tdis <dis:
								dis=tdis
			return dis
		elif  method=="complete":
			dis=0
			for i in dataset:
				if i.id[0] in x.id:
					tdis=0
					for j in dataset:
						if j.id[0] in y.id:
							tdis=round(np.sqrt(np.sum(np.power((i.value-j.value),2),axis=0)),2)
							if tdis >dis:
								dis=tdis
			return dis
		elif method=="Average":
			dis=0
			for i in dataset:
				if i.id[0] in x.id:
					for j in dataset:
						if j.id[0] in y.id:
							dis+=round(np.sqrt(np.sum(np.power((i.value-j.value),2),axis=0)),2)
			dis=dis/(x.count*y.count)
			return dis
		else:
			print("Error method")



	def minDist(self,dataset,method):
		#计算所有节点中距离最小的节点对
		mindist = 1000
		for i in range(len(dataset)-1):
			if dataset[i].check == 1:
				#略过合并过的节点
				continue
			for j in range(i+1,len(dataset)):
				if dataset[j].check == 1:
					continue
				dist = self.distance(dataset[i],dataset[j],dataset[0:80],method)
				if dist < mindist:
					mindist = dist
					x, y = i, j
		return mindist, x, y
		#返回最小距离、距离最小的两个节点的索引

	def fit(self,data,method):
		dataset = [clusterNode(value=item,id=["a"+str(i)],count=1) for i,item in enumerate(data)]
		#将输入的数据元素转化成节点，并存入节点的列表
		length = len(dataset)
		Backup = copy.deepcopy(dataset)
		#备份数据
		while(True):
			mindist, x, y = self.minDist(dataset,method)
			dataset[x].check = 1
			dataset[y].check = 1
			tmpid = copy.deepcopy(dataset[x].id)
			tmpid.extend(dataset[y].id)
			dataset.append(clusterNode(value=(dataset[x].value+dataset[y].value)/2,id=tmpid,\
				left=dataset[x],right=dataset[y],distance=mindist,count=dataset[x].count+dataset[y].count))
			#生成新节点
			if len(tmpid) == length:
				#当新生成的节点已经包含所有元素时，退出循环，完成聚类
				break
		#print("dataset shape",np.shape(dataset))
		#for item in dataset:
			#item.show()
		return dataset

	def show(self,dataset,num):
		showqueue = queue.Queue()
		#存放节点信息的队列
		showqueue.put(dataset[len(dataset) - 1])
		#存入根节点
		showqueue.put(num)
		#存入根节点的中心横坐标
		while not showqueue.empty():
			index = showqueue.get()
			#当前绘制的节点
			i = showqueue.get()
			#当前绘制节点中心的横坐标
			left = i - (index.count)/2
			right = i + (index.count)/2
			if index.left != None:
				x = [left,right]
				y = [index.distance,index.distance]
				plt.plot(x,y)
				x = [left,left]
				y = [index.distance,index.left.distance]
				plt.plot(x,y)
				showqueue.put(index.left)
				showqueue.put(left)
			if index.right != None:
				x = [right,right]
				y = [index.distance,index.right.distance]
				plt.plot(x,y)
				showqueue.put(index.right)
				showqueue.put(right)


def hct(data,k,method,isshow=False):
	ht = hcluster()

	resultt=ht.fit(data.values,method)
	if isshow:
		ht.show(resultt,np.shape(data.values)[0])

	cl=[]
	lcenter=[]
	for i in range(k-1):
		f=resultt[len(resultt)-1-i]
		l=f.left
		r=f.right
		for j in range(len(cl)):
			if cl[j]==f.id:
				cl.remove(cl[j])
				lcenter.pop(j)
				break
		cl.append(l.id)
		lcenter.append(l.value)
		cl.append(r.id)
		lcenter.append(r.value)
	lable=[]
	for j in resultt[:np.shape(data.values)[0]]:
		for i in range(k):
			if j.id[0] in cl[i]:
				lable.append(i+1)

	center=np.ndarray((k,2))
	for i in range(k):
		center[i]=lcenter[i]

	#print(np.shape(lable))
	#print(lable)
	#print(center)
	return lable,center


if __name__ == '__main__':

	import pandas as pd

	data = pd.read_csv('data.txt',sep=' ')

	k=int(input("请输入类别数"))
	kind=input("请输入类间距离方式(single/complete/Average)")
	plt.figure(1)
	lable,center=hct(data,k,kind,isshow=True)
	plt.figure(2)
	plt.subplot(121)
	plt.scatter(data.iloc[:,0],data.iloc[:,1],c="b")
	plt.subplot(122)
	plt.scatter(data.iloc[:,0],data.iloc[:,1],c=lable[:80])

	y=[]
	for i in range(2,10):
		#plt.figure(i+1)
		lable,center=hct(data,i,kind)
		sum=0
		for j in range(len(data.values)):
			#print((center[lable[j]-1,:0]).dtype)
			#print(type(data.iloc[j,:].values-center[lable[j]-1,:]))
			sum+=round(np.sqrt(np.sum(np.power(data.iloc[j,:].values-center[lable[j]-1,:],2))),2)
		y.append(sum)
	plt.figure(i+1)
	plt.scatter(range(2,10),y,c="r")
	plt.plot(range(2,10),y)
	plt.show()
