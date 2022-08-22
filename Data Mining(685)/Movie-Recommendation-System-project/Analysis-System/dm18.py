#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Lead Actor']
act=[k for k in df.actor_name]
actor=set(act)
ver=[k for k in df.verdict]
verdict=set(ver)
verdict.remove(np.nan)
verdict=list(verdict)
data=[]
v0=0
v1=0
v2=0
v3=0
v4=0
v5=0
v6=0
v7=0
v8=0
a0=''
a1=''
a2=''
a3=''
a4=''
a5=''
a6=''
a7=''
a8=''

for i in actor:
    dk=df[df['actor_name']==i]

    dj=dk[dk.verdict==verdict[0]]
    if len(dj)>v0:
        v0=len(dj)
        a0=i
    
    dj=dk[dk.verdict==verdict[1]]
    if len(dj)>v1:
        v1=len(dj)
        a1=i
        
    dj=dk[dk.verdict==verdict[2]]
    if len(dj)>v2:
        v2=len(dj)
        a2=i
        
    dj=dk[dk.verdict==verdict[3]]
    if len(dj)>v3:
        v3=len(dj)
        a3=i
        
    dj=dk[dk.verdict==verdict[4]]
    if len(dj)>v4:
        v4=len(dj)
        a4=i
        
    dj=dk[dk.verdict==verdict[5]]
    if len(dj)>v5:
        v5=len(dj)
        a5=i
        
    dj=dk[dk.verdict==verdict[6]]
    if len(dj)>v6:
        v6=len(dj)
        a6=i
        
    dj=dk[dk.verdict==verdict[7]]
    if len(dj)>v7:
        v7=len(dj)
        a7=i
        
    dj=dk[dk.verdict==verdict[8]]
    if len(dj)>v8:
        v8=len(dj)
        a8=i
        

data=[]
data.append(['Most '+verdict[0]+'s',a0,v0])
data.append(['Most '+verdict[1]+'s',a1,v1])
data.append(['Most '+verdict[2]+'s',a2,v2])
data.append(['Most '+verdict[3]+'s',a3,v3])
data.append(['Most '+verdict[4]+'s',a4,v4])
data.append(['Most '+verdict[5]+'s',a5,v5])
data.append(['Most '+verdict[6]+'s',a6,v6])
data.append(['Most '+verdict[7]+'s',a7,v7])
data.append(['Most '+verdict[8]+'s',a8,v8])

data = pd.DataFrame(data, columns = ['Title','actor','no. of movies']) 
data=data.sort_values('no. of movies')
data=data.set_index('Title')
data.to_csv('output-files/actors-movies-verdict.csv')


df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Director']
act=[k for k in df.actor_name]
actor=set(act)
ver=[k for k in df.verdict]
verdict=set(ver)
verdict.remove(np.nan)
verdict=list(verdict)
data=[]
v0=0
v1=0
v2=0
v3=0
v4=0
v5=0
v6=0
v7=0
v8=0
a0=''
a1=''
a2=''
a3=''
a4=''
a5=''
a6=''
a7=''
a8=''

for i in actor:
    dk=df[df['actor_name']==i]

    dj=dk[dk.verdict==verdict[0]]
    if len(dj)>v0:
        v0=len(dj)
        a0=i
    
    dj=dk[dk.verdict==verdict[1]]
    if len(dj)>v1:
        v1=len(dj)
        a1=i
        
    dj=dk[dk.verdict==verdict[2]]
    if len(dj)>v2:
        v2=len(dj)
        a2=i
        
    dj=dk[dk.verdict==verdict[3]]
    if len(dj)>v3:
        v3=len(dj)
        a3=i
        
    dj=dk[dk.verdict==verdict[4]]
    if len(dj)>v4:
        v4=len(dj)
        a4=i
        
    dj=dk[dk.verdict==verdict[5]]
    if len(dj)>v5:
        v5=len(dj)
        a5=i
        
    dj=dk[dk.verdict==verdict[6]]
    if len(dj)>v6:
        v6=len(dj)
        a6=i
        
    dj=dk[dk.verdict==verdict[7]]
    if len(dj)>v7:
        v7=len(dj)
        a7=i
        
    dj=dk[dk.verdict==verdict[8]]
    if len(dj)>v8:
        v8=len(dj)
        a8=i
        

data=[]
data.append(['Most '+verdict[0]+'s',a0,v0])
data.append(['Most '+verdict[1]+'s',a1,v1])
data.append(['Most '+verdict[2]+'s',a2,v2])
data.append(['Most '+verdict[3]+'s',a3,v3])
data.append(['Most '+verdict[4]+'s',a4,v4])
data.append(['Most '+verdict[5]+'s',a5,v5])
data.append(['Most '+verdict[6]+'s',a6,v6])
data.append(['Most '+verdict[7]+'s',a7,v7])
data.append(['Most '+verdict[8]+'s',a8,v8])

data = pd.DataFrame(data, columns = ['Title','director','no. of movies']) 
data=data.sort_values('no. of movies')
data=data.set_index('Title')
data.to_csv('output-files/directors-movies-verdict.csv')


df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Producer']
act=[k for k in df.actor_name]
actor=set(act)
ver=[k for k in df.verdict]
verdict=set(ver)
verdict.remove(np.nan)
verdict=list(verdict)
data=[]
v0=0
v1=0
v2=0
v3=0
v4=0
v5=0
v6=0
v7=0
v8=0
a0=''
a1=''
a2=''
a3=''
a4=''
a5=''
a6=''
a7=''
a8=''

for i in actor:
    dk=df[df['actor_name']==i]

    dj=dk[dk.verdict==verdict[0]]
    if len(dj)>v0:
        v0=len(dj)
        a0=i
    
    dj=dk[dk.verdict==verdict[1]]
    if len(dj)>v1:
        v1=len(dj)
        a1=i
        
    dj=dk[dk.verdict==verdict[2]]
    if len(dj)>v2:
        v2=len(dj)
        a2=i
        
    dj=dk[dk.verdict==verdict[3]]
    if len(dj)>v3:
        v3=len(dj)
        a3=i
        
    dj=dk[dk.verdict==verdict[4]]
    if len(dj)>v4:
        v4=len(dj)
        a4=i
        
    dj=dk[dk.verdict==verdict[5]]
    if len(dj)>v5:
        v5=len(dj)
        a5=i
        
    dj=dk[dk.verdict==verdict[6]]
    if len(dj)>v6:
        v6=len(dj)
        a6=i
        
    dj=dk[dk.verdict==verdict[7]]
    if len(dj)>v7:
        v7=len(dj)
        a7=i
        
    dj=dk[dk.verdict==verdict[8]]
    if len(dj)>v8:
        v8=len(dj)
        a8=i
        

data=[]
data.append(['Most '+verdict[0]+'s',a0,v0])
data.append(['Most '+verdict[1]+'s',a1,v1])
data.append(['Most '+verdict[2]+'s',a2,v2])
data.append(['Most '+verdict[3]+'s',a3,v3])
data.append(['Most '+verdict[4]+'s',a4,v4])
data.append(['Most '+verdict[5]+'s',a5,v5])
data.append(['Most '+verdict[6]+'s',a6,v6])
data.append(['Most '+verdict[7]+'s',a7,v7])
data.append(['Most '+verdict[8]+'s',a8,v8])

data = pd.DataFrame(data, columns = ['Title','producer','no. of movies']) 
data=data.sort_values('no. of movies')
data=data.set_index('Title')
data.to_csv('output-files/producers-movies-verdict.csv')





