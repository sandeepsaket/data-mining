#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import datetime
df=pd.read_csv('boxoffice_movies.csv')
df['year'] = pd.DatetimeIndex(df['release_date']).year
df=df.filter(['movie_id','name','total_nett_gross','overseas_gross','footfalls','year'])
years=[i for i in df.year]
year = []
for i in years:
    if i not in year:
        year.append(i)
year=year[0:-1]
data=[]
for i in year:
    dk=df[df.year==i]
    ind=dk['total_nett_gross'].idxmax()
    maxnet=dk['name'][ind]
    
    ind=dk['overseas_gross'].idxmax()
    maxo=dk['name'][ind]
    
    ind=dk['footfalls'].idxmax()
    maxf=dk['name'][ind]
    
    data.append([i,maxnet,maxo,maxf])
    
df1=pd.read_csv('boxoffice_actors.csv')
df1=df1[df1['role']=='Lead Actor']

df = pd.merge(df, df1, how="inner", on=["movie_id"])  

df=df.filter(['movie_id','total_nett_gross','overseas_gross','footfalls','year','actor_name'])
  
    
dataset=[]
for i in year:
    dk=df[df.year==i]
    netsum=0
    acnet=''
    neto=0
    aco=''
    netf=0
    acf=''
    act=[]
    act=[k for k in dk.actor_name]
    actor=set(act)
    
    
    
    for j in actor:
        dj=dk[dk['actor_name']==j]
        sumnet=dj['total_nett_gross'].sum()
        if sumnet>netsum:
            netsum=sumnet
            acnet=j
        sumo=dj['overseas_gross'].sum()
        if sumo>neto:
            neto=sumo
            aco=j
            
        sumf=dj['footfalls'].sum()
        if sumf>netf:
            netf=sumf
            acf=j
            
    dataset.append([i,acnet,aco,acf])
        
data = pd.DataFrame(data, columns = ['year', 'nettindia_movies','overseas_movies','footfalls_movies'])        
dataset=pd.DataFrame(dataset, columns = ['year', 'nettindia_actors','overseas_actors','footfalls_actors'])  
data=data.sort_values('year',ascending=False)
dataset=dataset.sort_values('year',ascending=False)
data.to_csv('output-files/yearwise-highest-movies.csv',index=False)

dataset.to_csv('output-files/yearwise-highest-actors.csv',index=False)   





