''' Backpropagation for the ANN'''
import numpy as np
from numpy import random
from numpy.core.fromnumeric import size
X= np.array(([2,9], [1,5], [3,6]),dtype= float)
y = np.array(([92],[86],[89]), dtype= float)

# normalization
X= X/np.amax(X, axis=0)
y= y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

#initialise the data

epoch = 7000
lr= 0.1
#number of nurons in layers
ip_l =2
hi_l=3
op_l= 1

wh = np.random.uniform(size=(ip_l,hi_l))
bh = np.random.uniform(size= (1,hi_l))
wout= np.random.uniform(size = (hi_l,op_l))
bout= np.random.uniform(size= (1,op_l))


for i in range(epoch):
    #forward propageation
    hinp1= np.dot(X,wh)
    hinp= hinp1+bh
    hlayer_act= sigmoid(hinp)
    outinp1= np.dot(hlayer_act,wout)
    outinp= outinp1+bout
    output = sigmoid(outinp)

    #back propagation
    EO = y- output
    outgrad= derivative_sigmoid(output)
    d_output= EO*outgrad
    EH= d_output.dot(wout.T)
    hiddengrad= derivative_sigmoid(hlayer_act)
    d_hidden_layer= EH*hiddengrad
    #updation of the weights
    wout += hlayer_act.T.dot(d_output)
    wh+= X.T.dot(d_hidden_layer)*lr
print('...............................................................................')
print("Input: \n"+str(X))
print("\n\nActual Output: \n"+ str(y))
print ("\n\nPredicted Output: \n"+ str(output))
print('\n'*2)