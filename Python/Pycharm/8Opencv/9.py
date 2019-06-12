import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('test.png')
rows,cols,ch=image.shape
tall=image[0:66,0:135]
image[67:133,136:271]=tall
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
