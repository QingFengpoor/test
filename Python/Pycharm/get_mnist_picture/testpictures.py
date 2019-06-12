import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("MNIST_data/train/mnist_train_0_5.jpg",0)
plt.imshow(image,cmap=plt.cm.gray)
plt.axis("off")
plt.show()
