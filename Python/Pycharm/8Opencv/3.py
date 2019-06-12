import cv2
img=cv2.imread('test.png')
print(img.shape) #(768,1024,3)
print(img.size )#2359296 768*1024*3
print(img.dtype) #uint8
