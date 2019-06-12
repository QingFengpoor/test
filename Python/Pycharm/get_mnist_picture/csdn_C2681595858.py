# pythonBP.py

import numpy as np
import random
import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
import time

# Sigmoid函数，S型曲线，
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))
# Sigmoid函数的导函数
def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))
#Tanh函数
def tanh(z):
    return np.tanh(z)
def tanh_prime(z):
    return 1.0-tanh(z)**2


class NeuralNet(object):

    # 初始化神经网络，sizes是神经网络的层数和每层神经元个数
    def __init__(self, sizes,ofunction="sigmoid",alpha=0.0):
        self.sizes_ = sizes
        self.num_layers_ = len(sizes)  # 层数
        self.w_ = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]  # w_、b_初始化为正态分布随机数
        self.b_ = [np.random.randn(y, 1) for y in sizes[1:]]
        self.alpha=alpha
        if ofunction=="sigmoid":
            self.ofunction=sigmoid
            self.ofunction_prime=sigmoid_prime
        elif ofunction=="tanh":
            self.ofunction=tanh
            self.ofunction_prime=tanh_prime


    def feedforward(self, x):
        for b, w in zip(self.b_, self.w_):
            x = self.ofunction(np.dot(w, x) + b)
        return x

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.b_]
        nabla_w = [np.zeros(w.shape) for w in self.w_]

        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.b_, self.w_):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = self.ofunction(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) * \
            self.ofunction_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers_):
            z = zs[-l]
            sp = self.ofunction_prime(z)
            delta = np.dot(self.w_[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.b_]
        nabla_w = [np.zeros(w.shape) for w in self.w_]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.w_ = [w-(eta/len(mini_batch))*nw-self.alpha*w for w, nw in zip(self.w_, nabla_w)]
        self.b_ = [b-(eta/len(mini_batch))*nb-self.alpha*b for b, nb in zip(self.b_, nabla_b)]

    # training_data是训练数据(x, y);epochs是训练次数;mini_batch_size是每次训练样本数;eta是learning rate
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)

        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

    # 预测
    def predict(self, data):
        value = self.feedforward(data)
        return value.tolist().index(max(value))

    # 保存训练模型
    def save(self):
        pass  # 把_w和_b保存到文件(pickle)
    def load(self):
        pass

def load_mnist(dataset="training_data", digits=np.arange(10), path="."):

    if dataset == "training_data":
        fname_image = os.path.join(path, 'MNIST_data/train-images.idx3-ubyte')
        fname_label = os.path.join(path, 'MNIST_data/train-labels.idx1-ubyte')
    elif dataset == "testing_data":
        fname_image = os.path.join(path, 'MNIST_data/t10k-images.idx3-ubyte')
        fname_label = os.path.join(path, 'MNIST_data/t10k-labels.idx1-ubyte')
    else:
        raise ValueError("dataset must be 'training_data' or 'testing_data'")

    flbl = open(fname_label, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = pyarray("b", flbl.read())
    flbl.close()

    fimg = open(fname_image, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = pyarray("B", fimg.read())
    fimg.close()

    ind = [ k for k in range(size) if lbl[k] in digits ]
    N = len(ind)

    images = zeros((N, rows, cols), dtype=uint8)
    labels = zeros((N, 1), dtype=int8)
    for i in range(len(ind)):
        images[i] = array(img[ ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))
        labels[i] = lbl[ind[i]]

    return images, labels

def load_samples(dataset="training_data"):

    image,label = load_mnist(dataset)

    X = [np.reshape(x,(28*28, 1)) for x in image]
    X = [x/255.0 for x in X]   # 灰度值范围(0-255)，转换为(0-1)

    # 5 -> [0,0,0,0,0,1.0,0,0,0];  1 -> [0,1.0,0,0,0,0,0,0,0]
    def vectorized_Y(y):
        e = np.zeros((10, 1))
        e[y] = 1.0
        return e

    if dataset == "training_data":
        Y = [vectorized_Y(y) for y in label]
        pair = list(zip(X, Y))
        return pair
    elif dataset == 'testing_data':
        pair = list(zip(X, label))
        return pair
    else:
        print('Something wrong')

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

def get_train(num):
    import cv2
    X_data=[]
    for i in range(num):
        img=cv2.imread("MNIST_data/train/mnist_train_%d.jpg"%i)
        r,g,b=[img[:,:,i] for i in range(3)]
        img_gray=r*0.299+g*0.587+b*0.114
        #th=OTSU_enhance(img_gray)
        #for i in range(img_gray.shape[0]):
        #    for j in range(img_gray.shape[1]):
        #        if img_gray[i][j]>th:
        #            img_gray[i][j]=255
        #        else:
        #            img_gray[i][j]=0
        img_gray_1D=np.array(img_gray).reshape(-1,1)/255
        X_data.append(img_gray_1D)
    X_data = np.array(X_data)
    y_data=[]
    with open('MNIST_data/mnist_train_label.txt','r') as f:
        for i in range(num):
            r=np.zeros((10,1))
            r[int(float(f.readline().strip()))]=1.0
            y_data.append(r)
            #y_data.append(float(f.readline().strip()))
    y_data=np.array(y_data)
    return [(X,y) for X,y in zip(X_data,y_data)]

def get_test():
    import cv2
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

if __name__ == '__main__':
    start=time.clock()
    INPUT = 28*28
    OUTPUT = 10
    net = NeuralNet([INPUT, 40, OUTPUT],ofunction="sigmoid",alpha=0.0)#传进去的是一个链表，分别表示每一层的神经元个数，而链表的长度刚好就是神经网络的层数

    train_set = load_samples(dataset='training_data')
    test_set = load_samples(dataset='testing_data')

    train_set_img=get_train(60000)
    test_set_img=get_test()


    net.SGD(train_set, 13, 100, 3.0, test_data=test_set_img)

    #准确率
    correct = 0;
    for test_feature in test_set_img:
        if net.predict(test_feature[0]) == test_feature[1][0]:
            correct += 1
    print("准确率: ", correct/len(test_set_img))
    print("运行时间：",time.clock()-start)
