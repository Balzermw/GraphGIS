import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/michael/Documents/2016-11.csv')

BBox = ((df.longitude.min(),   
		df.longitude.max(),      
         df.latitude.min(),
          df.latitude.max()))

print(BBox)


ruh_m = plt.imread('/Users/michael/Documents/map.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Where I drove in November 2016')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')




