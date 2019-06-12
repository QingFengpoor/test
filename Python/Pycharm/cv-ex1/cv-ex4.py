#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def OTSU_enhance(img_gray, th_begin=0, th_end=256, th_step=1):
    assert img_gray.ndim == 2, "must input a gary_img"

    max_g = 0
    suitable_th = 0
    for threshold in range(th_begin, th_end, th_step):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue

        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix
        # intra-class variance
        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold
    return suitable_th

img = cv2.imread("./img.jpg") #读取图像
img=img[:,:,(2,1,0)]
r,g,b = [img[:,:,i] for i in range(3)]
img_gray = r*0.299+g*0.587+b*0.114

th=OTSU_enhance(img_gray)
img_gray_01=img_gray.copy()
img_gray_01[img_gray_01<=th]=0
img_gray_01[img_gray_01>th]=1

#print(th)
plt.subplot(121)
plt.imshow(img_gray,cmap="gray")
plt.title("灰度图")
plt.subplot(122)
plt.imshow(img_gray_01,cmap="gray")
plt.title("二值图")
plt.show()
