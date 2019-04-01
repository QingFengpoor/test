#scipy图像处理
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
from scipy import misc
#1、图片的处理
#用ascent创建图片
image = misc.ascent()

# 显示全部图片
aa = plt.subplot(221)
plt.title("title")
plt.imshow(image)
plt.axis('off')

#使用scipy的中值滤波处理图片
plt.subplot(222)
plt.title("filter")
filter = ndimage.median_filter(image,size=10)
plt.imshow(filter)
plt.axis('off')

# 旋转
plt.subplot(223)
rotate = ndimage.rotate(image,180)
plt.title("rotate")
plt.imshow(rotate)
plt.axis('off')

# 边缘检测
plt.subplot(224)
prewitt = ndimage.prewitt(image)
plt.title("prewitt")
plt.imshow(prewitt)
plt.axis('off')
plt.show()
#2、加载本地图片
# 图片和代码同一个目录
lena = mpimg.imread('IMG_20190201_173614.jpg')
plt.title("load_jpg")
plt.imshow(lena)
plt.axis('off')
plt.show()
