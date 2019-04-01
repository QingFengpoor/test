import scipy
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt


num_px = 64

image = plt.imread("IMG_20190201_173614.jpg")
#my_image = scipy.misc.imresize(image, size=(num_px,num_px))
plt.imshow(image)
#plt.imshow(my_image)
plt.show();

