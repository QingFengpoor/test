import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('test.jpg')
rows,cols,ch=image.shape #拆分通道，cv2.split()是一个比较耗时的操作。只有需要时使用，尽量Numpy
b,g,r=cv2.split(image)
print(b.shape) #(768,1024) #合并通道
image=cv2.merge(b,g)
#image=cv2.merge(image,r)
print(image.shape)

import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('test.jpg')
rows,cols,ch=image.shape #直接获取
b=image[:,:,0]


