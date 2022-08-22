#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import datetime
df=pd.read_csv('boxoffice_movies.csv')
dk=pd.read_csv('boxoffice_actors.csv')
dk=dk[dk['role']=='Lead Actor']
df = pd.merge(df, dk, how="inner", on=["movie_id"]) 
df['year'] = pd.DatetimeIndex(df['release_date']).year
act=[k for k in df.actor_name]
actor=set(act)
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    date=dj['release_date'].min()
    dj2=dj.loc[dj['release_date'] == date]
    k=dj2['name'].to_list()
    name=k[0]
    ki=dj2['year'].to_list()
    year=ki[0]
    data.append([i,name,year])
    
data=pd.DataFrame(data, columns = ['actor', 'debut movie','debut year'])  
data=data.sort_values('actor')
data.to_csv('output-files/actors-debut.csv',index=False)

df=pd.read_csv('boxoffice_movies.csv')
dk=pd.read_csv('boxoffice_actors.csv')
dk=dk[dk['role']=='Director']
df = pd.merge(df, dk, how="inner", on=["movie_id"]) 
df['year'] = pd.DatetimeIndex(df['release_date']).year
act=[k for k in df.actor_name]
actor=set(act)
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    date=dj['release_date'].min()
    dj2=dj.loc[dj['release_date'] == date]
    k=dj2['name'].to_list()
    name=k[0]
    ki=dj2['year'].to_list()
    year=ki[0]
    data.append([i,name,year])
    
data=pd.DataFrame(data, columns = ['director', 'debut movie','debut year'])  
data=data.sort_values('director')
data.to_csv('output-files/directors-debut.csv',index=False)

df=pd.read_csv('boxoffice_movies.csv')
dk=pd.read_csv('boxoffice_actors.csv')
dk=dk[dk['role']=='Producer']
df = pd.merge(df, dk, how="inner", on=["movie_id"]) 
df['year'] = pd.DatetimeIndex(df['release_date']).year
act=[k for k in df.actor_name]
actor=set(act)
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    date=dj['release_date'].min()
    dj2=dj.loc[dj['release_date'] == date]
    k=dj2['name'].to_list()
    name=k[0]
    ki=dj2['year'].to_list()
    year=ki[0]
    data.append([i,name,year])
    
data=pd.DataFrame(data, columns = ['producer', 'debut movie','debut year'])  
data=data.sort_values('producer')
data.to_csv('output-files/producers-debut.csv',index=False)





