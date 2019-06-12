## 转载自：https://www.cnblogs.com/lynsyklate/p/7881300.html

import cv2 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

plt.subplot(121)
plt.title("origin")
saber=cv2.imread("saber.png")
##print(saber.shape)
saber=cv2.cvtColor(saber,cv2.COLOR_BGR2RGB)
plt.imshow(saber)
plt.axis("off")

gray_saber=cv2.cvtColor(saber,cv2.COLOR_BGR2GRAY)
gray_saber=cv2.resize(gray_saber,(200,200))
##print(gray_saber.shape)

##Robert算子
def RobertsOperator(roi):
    operator_first=np.array([[-1,0],[0,1]])
    operator_second=np.array([[0,-1],[1,0]])
    return np.abs(np.sum(roi[1:,1:]*operator_first))+np.abs(np.sum(roi[1:,1:]*operator_second))

def RobertsAlogrithm(image):
    image=cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range (1,image.shape[0]):
        for j in range(1,image.shape[1]):
            image[i,j]=RobertsOperator(image[i-1:i+2,j-1:j+2])
    return image[1:image.shape[0],1:image.shape[1]]

Robert_saber=RobertsAlogrithm(gray_saber)
##print(Robert_saber.shape)
plt.subplot(122)
plt.title("Robert")
plt.imshow(Robert_saber,cmap="binary")
plt.axis("off")
plt.show()

##Robert增加噪声
def noisy(noise_type,image):
    if noise_type=="gauss":
        row,col,ch=image.shape
        mean=0
        var=0.1
        sigma=var**0.5
        gauss=np.random.normal(mean,sigma,(row,col,ch))
        gauss=gauss.reshape(row,col,ch)
        noisy=image+gauss
        return noisy
    elif noise_type=="s&p":
        row,col,ch=image.shape
        s_vs_p=0.5
        amount=0.004
        out=np.copy(image)
        num_salt=np.ceil(amount*image.size*s_vs_p)
        coords=[np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
        out[tuple(coords)]=1
        num_pepper=np.ceil(amount*image.size*(1.-s_vs_p))
        coords=[np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
        out[tuple(coords)]=0
        return out
    elif noise_type=="poisson":
        vals=len(np.unique(image))
        vals=2**np.ceil(np.log2(vals))
        noisy=np.random.poisson(image*vals)/float(vals)
        return noisy
    elif noise_type=="speckle":
        row,col,ch=image.shape
        gauss=np.random.randn(row,col,ch)
        gauss=gauset_string_function.reshape(row,col,ch)
        noisy=image+image*gauss
        return noisy
    else:
        print('noise_type=="gauss"||"s&p"||"poisson"||"speckle"')

dst=noisy("s&p",saber)
##print(dst.shape)
plt.subplot(121)
plt.title("add s&p noise")
plt.axis("off")
plt.imshow(dst)
plt.subplot(122)
dst=cv2.cvtColor(dst,cv2.COLOR_RGB2GRAY)
##print(dst.shape)
plt.title("Robert Process")
plt.axis("off")
dst=RobertsAlogrithm(dst)
##print(dst.shape)
plt.imshow(dst,cmap="binary")
plt.show()

##PreWitt算子
def PreWittOperator(roi,operator_type):
    if operator_type=="horizontal":
        prewitt_operator=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    elif operator_type=="vertical":
        prewitt_operator=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    else:
        raise("type Error")
    result=np.abs(np.sum(roi*prewitt_operator))
    return result

def PreWittAlogrithm(image,operator_type):
    new_image=np.zeros(image.shape)
    image=cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1]=PreWittOperator(image[i-1:i+2,j-1:j+2],operator_type)
    new_image=new_image*(255/np.max(image))
    return new_image.astype(np.uint8)

plt.subplot(121)
plt.title("horizontal")
plt.imshow(PreWittAlogrithm(gray_saber,"horizontal"),cmap="binary")
plt.axis("off")
plt.subplot(122)
plt.title("vertical")
plt.imshow(PreWittAlogrithm(gray_saber,"vertical"),cmap="binary")
plt.axis("off")
plt.show()

##Prewitt 增加噪声
dst=noisy("s&p",saber)
plt.subplot(131)
plt.title("add noise")
plt.axis("off")
plt.imshow(dst)

plt.subplot(132)
plt.title("Prewitt horizontal")
plt.axis("off")
plt.imshow(PreWittAlogrithm(gray_saber,"horizontal"),cmap="binary")

plt.subplot(133)
plt.title("Prewitt Vertical")
plt.axis("off")
plt.imshow(PreWittAlogrithm(gray_saber,"vertical"),cmap="binary")
plt.show()

##Sobel算子
def SobelOperator(roi,operator_type):
    if operator_type=="horizontal":
        sobel_operator=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    elif operator_type=="vertical":
        sobel_operator=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    else:
        try:
            raise Exception("raise Exception")
        except Exception:
            print("raise an exception here")
            raise

    result=np.abs(np.sum(roi*sobel_operator))
    return result

def SobelAlogrithm(image,operator_type):
    new_image=np.zeros(image.shape)
    image=cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1]=SobelOperator(image[i-1:i+2,j-1:j+2],operator_type)
    new_image=new_image*(255/np.max(image))
    return new_image.astype(np.uint8)

plt.subplot(121)
plt.title("Sobel horizontal")
plt.imshow(SobelAlogrithm(gray_saber,"horizontal"),cmap="binary")
plt.axis("off")
plt.subplot(122)
plt.title("Sobel vertical")
plt.imshow(SobelAlogrithm(gray_saber,"vertical"),cmap="binary")
plt.axis("off")
plt.show()

##laplace 算子
def LaplaceOperator(roi,operator_type):
    if operator_type=="fourfields":
        laplace_operator=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    elif operator_type=="eightfields":
        laplace_operator=np.array([[1,1,1],[1,-8,1],[1,1,1]])
    else:
        raise("type Error")
    result=np.abs(np.sum(roi*laplace_operator))
    return result

def LaplaceAlogrithm(image,operator_type):
    new_image=np.zeros(image.shape)
    image=cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1]=LaplaceOperator(image[i-1:i+2,j-1:j+2],operator_type)
    new_image=new_image*(255/np.max(image))
    return new_image.astype(np.uint8)

plt.subplot(121)
plt.title("fourfields")
plt.imshow(LaplaceAlogrithm(gray_saber,"fourfields"),cmap="binary")
plt.axis("off")
plt.subplot(122)
plt.title("eightfields")
plt.imshow(LaplaceAlogrithm(gray_saber,"eightfields"),cmap="binary")
plt.axis("off")
plt.show()

##高斯模糊
def GaussianOperator(roi):
    GaussianKernel=np.array([[1,2,1],[2,4,2],[1,2,1]])
    result=np.sum(roi*GaussianKernel/16)
    return result

def GaussianSmooth(image):
    new_image=np.zeros(image.shape)
    image=cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            new_image[i-1,j-1]=GaussianOperator(image[i-1:i+2,j-1:j+2])
    return new_image.astype(np.uint8)

smooth_saber=GaussianSmooth(gray_saber)
plt.subplot(121)
plt.title("Origin Image")
plt.axis("off")
plt.imshow(gray_saber,cmap="gray")
plt.subplot(122)
plt.title("GaussianSmooth image")
plt.axis("off")
plt.imshow(smooth_saber,cmap="gray")
plt.show()

##计算梯度幅值和方向 G=sqrt(Gx**2+Gy**2) cita=atan2(Gy,Gx)
Gx=SobelAlogrithm(smooth_saber,"horizontal")
Gy=SobelAlogrithm(smooth_saber,"vertical")


G=np.sqrt(np.square(Gx.astype(np.float64))+np.square(Gy.astype(np.float64)))
cita=np.arctan2(Gy.astype(np.float64),Gx.astype(np.float64))
plt.imshow(G.astype(np.uint8),cmap="gray")
plt.title("梯度检测")
plt.axis("off")
plt.show()

##非极大值算法(抑制)
def NonmaximumSuppression(image,cita):
    keep=np.zeros(cita.shape)
    cita=np.abs(cv2.copyMakeBorder(cita,1,1,1,1,cv2.BORDER_DEFAULT))
    for i in range(1,cita.shape[0]-1):
        for j in range(1,cita.shape[1]-1):
            if cita[i][j]>cita[i-1][j] and cita[i][j]>cita[i+1][j]:
                keep[i-1][j-1]=1
            elif cita[i][j]>cita[i][j+1] and cita[i][j]>cita[i][j-1]:
                keep[i-1][j-1]=1
            elif cita[i][j]>cita[i+1][j+1] and cita[i][j]>cita[i-1][j-1]:
                keep[i-1][j-1]=1
            elif cita[i][j]>cita[i-1][j+1] and cita[i][j]>cita[i+1][j-1]:
                keep[i-1][j-1]=1
            else:
                keep[i-1][j-1]=0
    return keep*image
nms_image=NonmaximumSuppression(G,cita)
nms_image=(nms_image*(255/np.max(nms_image))).astype(np.uint8)

plt.imshow(nms_image,cmap="gray")
plt.axis("off")
plt.show()

##滞后阈值
MAXThreshold=np.max(nms_image)/4*3
MINThreshold=np.max(nms_image)/4 
usemap=np.zeros(nms_image.shape)
high_list=[]

for i in range(nms_image.shape[0]):
    for j in range(nms_image.shape[1]):
        if nms_image[i,j]>MAXThreshold:
            high_list.append((i,j))

direct=[(0,1),(1,1),(-1,1),(-1,-1),(1,0),(-1,0),(0,-1)]
def DFS(stepmap,start):
    route=[start]
    while route:
        now=route.pop()
        if usemap[now]==1:
            break
        usemap[now]=1
        for dic in direct:
            next_coodinate=(now[0]+dic[0],now[1]+dic[1])
            if not usemap[next_coodinate] and nms_image[next_coodinate]>MINThreshold \
                and next_coodinate[0]<stepmap.shape[0]-1 and next_coodinate[0]>=0 \
                and next_coodinate[1]<stepmap.shape[1]-1 and next_coodinate[1]>=0:
                route.append(next_coodinate)

for i in high_list:
    DFS(nms_image,i)

plt.imshow(nms_image*usemap,cmap="gray")
plt.axis("off")
plt.show()

def CannyAlogrithm(image,MINThreshold,MAXThreshold):
    image=GaussianSmooth(image)
    Gx=SobelAlogrithm(image,"horizontal")
    Gy=SobelAlogrithm(image,"vertical")
    G=np.sqrt(np.square(Gx.astype(np.float64))+np.square(Gy.astype(np.float64)))
    G=G*(255/np.max(G)).astype(np.uint8)
    cita=np.arctan2(Gy.astype(np._float64),Gx.astype(np.float64))
    num_image=NonmaximumSuppression(G,cita)
    nms_image=(nms_image*(255/np.max(nms_image))).astype(np.uint8)
    usemap=np.zeros(nms_image.shape)
    high_list=[]
    for i in range(nms_image.shape[0]):
        for j in range(nms_iamge.shape[1]):
            if nms_image[i,j]>MAXThreshold:
                high_list.append((i,j)) 

    direct=[(0,1),(1,1),(-1,1),(-1,-1),(1,-1),(1,0),(-1,0),(0,-1)]
    def DFS(stepmap,start):
        route=[start]
        while route:
            now=route.pop()
            if usemap[now]==1:
                break
            usemap[now]=1
            for dic in direct:
                next_coodinate=(now[0]+dic[0],now[1]+dic[1])
                if not usemap[next_coodinate] and nms_image[next_coodinate]>MINThreshold \
                    and next_coodinate[0]<stepmap.shape[0]-1 and next_coodinate[0]>=0 \
                    and next_coodinate[1]<stepmap.shape[1]-1 and next_coodinate[1]>=0:
                    route.append(next_coodinate)
    for i in high_list:
                DFS(nms_image,i)
    return nms_image*usemape