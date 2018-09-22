import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./HR_comma_sep.csv')

X = df['satisfaction_level']
y = df['number_project']


get_theta = lambda theta: np.array([[0, theta]])


def cost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2)
    print ('Inner', inner)
    cost = np.sum(inner) / (2 * len(X))
    print ('cost', cost)
    return cost

thetas = list(map(get_theta, [0.5, 1.0, 1.5]))

X = np.hstack([np.ones([3, 1]), X])