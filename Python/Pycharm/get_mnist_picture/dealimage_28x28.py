import numpy as np

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

def get_test():
    import cv2
    import os
    import copy
    if os.path.exists("test_28x28") is False:
        os.makedirs("test_28x28")
    X_data=[]
    for i in range(10):
        #img=cv2.imread("test/%d.jpg"%i,cv2.IMREAD_GRAYSCALE)二维的结果，行数个数组，每个数组长度为列数
        img=cv2.imread("test/%d.jpg"%i)
        t=len(img)
        while t/2.0>28 or t>28:
            img=cv2.pyrDown(img)
            t=len(img)
        img=cv2.resize(img,(28,28),interpolation=cv2.INTER_AREA)
        cv2.imwrite("test_28x28/%d.jpg"%i,img)
        b,g,r=[img[:,:,i] for i in range(3)]
        img_gray=r*0.299+g*0.587+b*0.114
        if np.sum(img_gray)>255*len(img_gray)/2:
            img_gray=color_reverse(img_gray)
        th=OTSU_enhance(img_gray)
        for i in range(img_gray.shape[0]):
            for j in range(img_gray.shape[1]):
                if img_gray[i][j]>th:
                    img_gray[i][j]=255
                else:
                    img_gray[i][j]=0
        img_gray_1D=np.array(img_gray).reshape(-1,1)/255
        X_data.append(img_gray_1D)
    X_data = np.array(X_data)
    y_data=[]
    for i in range(10):
        y_data.append(i)
    y_data=np.array(y_data).reshape(-1,1)
    return [(X,y) for X,y in zip(X_data,y_data)]

def color_reverse(img_array):
    img_reverse=255-img_array
    return img_reverse

test_img=get_test()
