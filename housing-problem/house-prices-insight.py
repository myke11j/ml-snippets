# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def findcost(X, y, theta):
   """ Calculates the cost function.
   Args:
       X (DataFrame): The design matrix
       y (DataFrame): The target
       theta (DataFrame): The hypothesis function's independent variables
   Returns:
       np.Array: the calculated squared error cost
   """
   m = len(y)
   o = pd.DataFrame(np.ones(m))
   errorSquared = (np.dot(X,theta)-y)**2
   return np.dot(o.T, errorSquared)/(2*m)

def gradientDescent(x, y, theta, alpha, m, numIterations):
   xTrans = x.transpose()
   for i in range(0, numIterations):
       hypothesis = np.dot(x, theta)
       print('h', hypothesis) 
       loss = hypothesis - y
       print('loss', loss)
       # avg cost per example (the 2 in 2*m doesn't really matter here.
       # But to be consistent with the gradient, I include it)
       cost = np.sum(loss ** 2) / (2 * m)
       print("Iteration %d | Cost: %f" % (i, cost))
       # avg gradient per example
       gradient = np.dot(xTrans, loss) / m
       # update
       theta = theta - alpha * gradient
       print("theta", (theta))
   return theta

df = pd.read_csv('./houseprices.csv')
[m, n] = df.shape
dfDesc = df.describe()

X = df.iloc[:, 12]
y = df.iloc[:, 13]

plt.scatter(X, y, c='g')
theta = np.ones(m)
alpha = 0.0005
numIterations=10000
# J = findcost(X, y, theta)
theta = gradientDescent(X, y, theta, alpha, m, numIterations)
print(theta)