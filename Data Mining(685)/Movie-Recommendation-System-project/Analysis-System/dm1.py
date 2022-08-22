#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


df=pd.read_csv('Data for repository.csv')

df=df.filter(['Movie Name','Number of Screens','Revenue(INR)','Budget(INR)','Genre'])
df.columns=['Movie Name','Number of Screens','Budget(INR) + Promotions','Gross Collections','Genre']

df['Profit Made through Box office']=df['Gross Collections']-df['Budget(INR) + Promotions']
df['Profit Percentage']=df['Profit Made through Box office']*100/df['Budget(INR) + Promotions']
df=df.sort_values('Profit Percentage',ascending=False)

df.index = np.arange(1, len(df) + 1)
df['Rankings'] = df.index


dfb=df.filter(['Rankings','Movie Name','Profit Percentage'])


dfc1=df.sort_values('Profit Made through Box office',ascending=False)
dfc1.index = np.arange(1, len(dfc1) + 1)
dfc1['Rankings'] = dfc1.index
dfc1=dfc1.filter(['Rankings','Movie Name','Profit Made through Box office'])

dfc2=df.sort_values('Gross Collections',ascending=False)
dfc2.index = np.arange(1, len(dfc2) + 1)
dfc2['Rankings'] = dfc2.index
dfc2=dfc2.filter(['Rankings','Movie Name','Gross Collections'])

dfb.to_csv('output-files/movie-ranking-profit-percent.csv', index = False)
dfc1.to_csv('output-files/movie-ranking-profit-made.csv', index = False)
dfc2.to_csv('output-files/movie-ranking-gross-collection.csv', index = False)

