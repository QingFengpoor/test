# Code for a 3-layer neural network, and code for learning the MNIST dataset
# Zhouxw@ebscn.com,2018.8  Studying to write neural network by python
# license is GPLv2

import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
import matplotlib.pyplot
# ensure the plots are inside this jupyter notebook, not an external window
#%matplotlib inline

# helper to load data from PNG image files
import imageio
# glob helps select multiple files using patterns
import glob

import cv2



# neural network class definition （3 layers）
class neuralNetwork:
    # initialise the neural network
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        # set number of nodes in each input,hidden,output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # learning rate
        self.lr = learningrate

        # link weight matrices ,wih and who
        # weithg inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = (numpy.random.normal(0.0, pow(self.hnodes,-0.5), (self.hnodes,self.inodes) )  )
        self.who = (numpy.random.normal(0.0, pow(self.onodes,-0.5), (self.onodes,self.hnodes) )  )

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # train the neural network
    def train(self,inputs_list,targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list,ndmin=2).T
        targets = numpy.array(targets_list,ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih,inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target-actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors,split by weights,recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

        pass

    # query the neural network
    def query(self,inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list,ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih,inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

# number of input,hidden and output nodes
# 28 * 28 = 784
input_nodes = 784
hidden_nodes = 200
output_nodes = 10

# learning rate is 0.3
learning_rate = 0.1

# create instance of neural network
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

# train the neural network

# load the mnist training data csv file into a list
#training_data_file = open("mnist_dataset/mnist_train.csv",'r')
#training_data_list = training_data_file.readlines()
#training_data_file.close()

N = 60000
X_train=[]
for i in range(N):
    img=cv2.imread("MNIST_data/train/mnist_train_%d.jpg"%i)
    r,g,b=[img[:,:,i] for i in range(3)]
    img_gray=r*0.299+g*0.587+b*0.114
    img_gray_1D=img_gray.flatten()
    #for i in range(len(img_gray_1D)):
    #    if img_gray_1D[i]<127:
    #        img_gray_1D[i]=0
    #    else:
    #        img_gray_1D[i]=1
    #img_gray_1D-=img_gray_1D.min()
    #img_gray_1D/=img_gray_1D.max()
    img_gray_1D=img_gray_1D/255.0*0.99+0.01
    X_train.append(img_gray_1D)
X_train = numpy.array(X_train)

Y_train=numpy.zeros((N,10))
Y_label=[]
with open('MNIST_data/mnist_train_label.txt','r') as f:
    for i in range(N):
        Y_label.append((int(float(f.readline().strip()))))
        Y_train[i]=0.01
        Y_train[i][(int(float(f.readline().strip())))]=0.99


# epochs is the number of times the training data set is used for training
epochs = 5
for e in range(epochs):
    # go through all records in the training data set
    for record in range(N):
        #all_values = record.split(',')
        # scale and shift the inputs
        #inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        #targets = numpy.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
        #targets[int(all_values[0])] = 0.99
        inputs=X_train[record]
        targets=Y_train[record]
        n.train(inputs,targets)
        pass
    pass

# test the neural network

# load the mnist test data csv file to a list
#test_data_file = open("mnist_dataset/mnist_test.csv",'r')
#test_data_list = test_data_file.readlines()
#test_data_file.close()
NT=1000
XT_train=[]
for i in range(NT):
    img=cv2.imread("MNIST_data/test/mnist_test_%d.jpg"%i)
    r,g,b=[img[:,:,i] for i in range(3)]
    img_gray=r*0.299+g*0.587+b*0.114
    img_gray_1D=img_gray.flatten()
    #for i in range(len(img_gray_1D)):
    #    if img_gray_1D[i]<127:
    #        img_gray_1D[i]=0
    #    else:
    #        img_gray_1D[i]=1
    #img_gray_1D-=img_gray_1D.min()
    #img_gray_1D/=img_gray_1D.max()
    img_gray_1D=img_gray_1D/255.0*0.99+0.01
    XT_train.append(img_gray_1D)
XT_train = numpy.array(XT_train)

YT_train=numpy.zeros((NT,10))
YT_label=[]
with open('MNIST_data/mnist_test_label.txt','r') as f:
    for i in range(NT):
        print(i,f.readline().strip())
        print(float(f.readline().strip()))
        YT_label.append((int(float(f.readline().strip()))))
        YT_train[i]=0.01
        YT_train[i][(int(float(f.readline().strip())))]=0.99

# scorecard for how well the network performs,initially empty
scorecard = []
# go through all records in the test data set
for record in range(NT):
    #all_values = record.split(',')
    # correct answer is first value
    #correct_label = int(all_values[0])
    # scale and shift the inputs
    #inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    inputs=XT_train[record]
    correct_label=YT_label[record]
    # query the network
    outputs = n.query(inputs)
    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
#    print("Answer label is:",correct_label," ; ",label," is network's answer")
    # append correct or incorrect to list
    if(label == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        scorecard.append(0)
    pass

# calculate the performance score ,the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size )
