# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('paytm_com-ecommerce_sample.csv')
dfHead = df.head()

# Number of bestsellers based in breadcrumbs
uniqueBreadcrumbs = df.breadcrumbs.unique()
groupedData = df.groupby(['discount'], as_index=False, level='ind').size()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = groupedData[0]
sizes = groupedData['Index']
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()