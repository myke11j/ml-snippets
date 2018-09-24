import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./HR_comma_sep.csv')

df = df[ df['Department'] == 'sales' ]
df = df.iloc[0:100,0:10]
X = df['satisfaction_level']
y = df['last_evaluation']

plt.scatter(X, y, c='g')