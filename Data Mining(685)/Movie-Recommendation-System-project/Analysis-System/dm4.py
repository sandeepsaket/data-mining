#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

df=pd.read_csv('indian movies.csv')
langs=df["Language"].to_list()
lang = []
for i in langs:
    if i not in lang:
        lang.append(i)
        
dataset=[]
for i in lang:
    dk=df[df["Language"]==i]
    count=dk.count()
    dk=dk[dk["Rating(10)"]!='-']
    dk["Rating(10)"] = pd.to_numeric(dk["Rating(10)"])
    
    high=dk["Rating(10)"].max()
    
    low=dk["Rating(10)"].min()
    
    avg=dk["Rating(10)"].mean()
    avg=round(avg,1)
    
    dataset.append([i,count[0],high,avg,low])

dataset = pd.DataFrame(dataset, columns = ['Language', 'Number of Movies','Highest Rating','Average Rating','Lowest Rating'])
dataset.sort_values('Number of Movies', ascending = False, inplace = True)
dataset.to_csv('output-files/language-movies.csv', index = False)

