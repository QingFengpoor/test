import cv2  # 利用opencv读取图像
import numpy as np
# 利用matplotlib显示图像
import matplotlib.pyplot as plt

img = cv2.imread("./img.jpg") #读取图像
img=img[:,:,(2,1,0)]
r,g,b = [img[:,:,i] for i in range(3)]
img_gray = r*0.299+g*0.587+b*0.114
# 显示图像
plt.figure("img_gray")
plt.imshow(img_gray,cmap="gray")
plt.axis('off')
plt.figure("img_gray_hist")

img_gray_1D = img_gray.flatten()
_,_,_ = plt.hist(img_gray_1D,bins=256,density=0)

#向量计算长度及对一维向量整数化
img_gray_1D_len = img_gray_1D.shape[0]
img_gray_1D_int = (img_gray_1D + 0.5).astype(np.uint8)

#建立一个像素占比的数组并计算
Psk = np.zeros(256)
for i in range(img_gray_1D.shape[0]):
    Psk[(img_gray_1D_int[i])] += 1
Psk = [Psk[i] / img_gray_1D_len for i in range(256)]
#计算每个像素累积概率
cdf = np.zeros(256)
cdf[0] = Psk[0]
for i in range(255):
    cdf[i + 1] = cdf[i] + Psk[i + 1]

#计算目标像素 并将一维向量还原成二维的灰度图
img_gray_1D_re = np.array([255 * cdf[img_gray_1D_int[i]] for i in range(len(img_gray_1D))])
img_re = img_gray_1D_re.reshape((img_gray_1D_len,-1))
#plt.figure("img_re")
#plt.imshow("img_re",cmap="gray")
plt.figure("img_re_hist")
_,_,_ = plt.hist(img_gray_1D_re,bins=256,density=0)

plt.show()
