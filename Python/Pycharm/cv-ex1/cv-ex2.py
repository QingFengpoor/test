# -*- coding: utf-8 -*-
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

def deal_image(path):
    im=io.imread(path,as_gray=True)
    io.imshow(im)
    plt.title(path+'_image_grey')
    plt.show()
    im_copy_med=io.imread(path, as_gray=True)
    im_copy_mea =io.imread(path, as_gray=True)
    im_copy_max=io.imread(path, as_gray=True)
    im_copy_min=io.imread(path, as_gray=True)
    #io.imshow(im)
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            im_copy_med[i][j]=im[i][j]
            im_copy_mea[i][j]=im[i][j]
            im_copy_max[i][j]=im[i][j]
            im_copy_min[i][j]=im[i][j]
    #定义滤波器
    return im,im_copy_med,im_copy_mea,im_copy_max,im_copy_min
im,im_copy_med,im_copy_mea,im_copy_max,im_copy_min=deal_image('img.jpg')
def m_filter(x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]
def max_filte(x,y,step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return max(sum_s)
def min_filte(x,y,step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return min(sum_s)
def mean_filter(x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s
#Step为滤波器的大小
def test(Step):
    for i in range(int(Step/2),im.shape[0]-int(Step/2)):
        for j in range(int(Step/2),im.shape[1]-int(Step/2)):
            im_copy_med[i][j] = m_filter(i, j, Step)
            im_copy_mea[i][j] = mean_filter(i, j, Step)
            im_copy_max[i][j]=max_filte(i,j,Step)
            im_copy_min[i][j]=min_filte(i,j,Step)
    io.imshow(im_copy_med)
    plt.title('median_image')
    plt.show()
    io.imsave(str(Step) + 'med.jpg', im_copy_med)
    io.imshow(im_copy_mea)
    plt.title('mean_image')
    plt.show()
    io.imsave(str(Step) + 'mea.jpg', im_copy_mea)
    io.imshow(im_copy_max)
    plt.title('max_image')
    plt.show()
    io.imsave(str(Step) + 'max.jpg', im_copy_max)
    io.imshow(im_copy_min)
    plt.title('min_image')
    io.imsave(str(Step) + 'min.jpg', im_copy_min)
    plt.show()

test(3)
