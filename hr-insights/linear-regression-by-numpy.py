#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 12:39:41 2018

@author: mukuljain
"""

import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([[1], [2.5], [3.5]])

get_theta = lambda theta: np.array([[0, theta]])

thetas = list(map(get_theta, [0.5, 1.0, 1.5]))

X = np.hstack([np.ones([3, 1]), X])

def cost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2)
    print ('Inner', inner)
    cost = np.sum(inner) / (2 * len(X))
    print ('cost', cost)
    return cost

for i in range(len(thetas)):
    print(cost(X, y, thetas[i]))