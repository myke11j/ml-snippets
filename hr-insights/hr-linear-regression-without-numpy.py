import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(dpi=120)
ax = plt.axes(projection='3d')

theta0List = []
theta1List = []
gradientList = []

def computeCost(m, theta0, theta1, x, y):
    totalError = 0;
    for i in range(0, m):
        if (x[i]):
            hypothesis = theta0 - (theta1 * x[i])
            error = hypothesis - y[i]
            totalError += error ** 2
    return totalError / m

# m denotes the number of examples here, not the number of features
def gradientDescent(x, y, theta0, theta1, learning_rate, num_iterations):
    m = len(x)
    theta0Gradient = 0;
    theta1Gradient = 0;
    for i in range(0, num_iterations):
        cost = computeCost(m, theta0, theta1, x, y)
        theta0List.append(theta0)
        theta1List.append(theta1)
        gradientList.append(cost)
        print("Iteration %d | Cost: %f" % (i, cost))
        theta0Gradient += -(2/m) * (y[i] - ((theta1 * x[i]) + theta0))
        theta1Gradient += -(2/m) * x[i] * (y[i] - ((theta1 * x[i]) + theta1))
        theta0 = theta0 - (learning_rate * theta0Gradient)
        theta1 = theta1 - (learning_rate * theta1Gradient)
    return [theta0, theta1]
    
def readFile():
    return pd.read_csv('./HR_comma_sep.csv')

def run():
    # Read dataset
    df = readFile();
    [m, n] = df.shape

    # Set hyper paramters
    learning_rate = 0.01
    # y = mx + b (slope formula) ~ theta1.x + theta0
    num_iterations = 1000
    theta0 = 0
    theta1 = 0
    
    # Train our model
    df = df[ df['Department'] == 'sales' ]
    df = df.reindex(pd.RangeIndex(df.index.max() + 1)).ffill()
    #  df = df.iloc[0:100,0:10]
    [m, n] = df.shape
    X = df['satisfaction_level']
    y = df['last_evaluation']
    
    print("Starting gradient descent at b = %d, m = %d, error = %f" % (theta0, theta1, computeCost(m, theta0, theta1, X, y)))
    print("Running...")
    [theta0, theta1] = gradientDescent(X, y, theta0, theta1, learning_rate, num_iterations)
    print("After %d iterations b = %f, m = %f, error = %f" % (num_iterations, theta0, theta1, computeCost(m, theta0, theta1, X, y)))
    ax.plot_trisurf(theta1List, theta0List, gradientList, color='green')


if __name__ == '__main__':
    run()