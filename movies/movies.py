# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('movies.csv')
dfHead = df.head()

df['prim_genre'] = df.genres.apply(lambda x: x.split('|')[0])

dfPrimaryGenreGroup = df.groupby(['prim_genre']).size()

dfPrimaryGenreGroup.plot.bar()