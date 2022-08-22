#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df=pd.read_csv('boxoffice_actors.csv')
mov=[k for k in df.movie_id]
mid=set(mov)
mid=list(mid)

fin=[]
for i in mid:
    dk=df[df['movie_id']==i]
    d=dk[dk['role']=='Director']
    direc=d['actor_name'].to_list()
    ng=d['nett_gross'].to_list()
    bgt=0
    if len(ng)!=0:
        bgt=ng[0]
        

    if len(direc)!=0:
        di=direc[0]
    else:
        di='na'
    
    a=dk[dk['role']=='Lead Actor']
    actor=a['actor_name'].to_list()
    for j in actor:
        fin.append([di,j,bgt])
    
data= pd.DataFrame(fin, columns = ['director','actor','tot nett gross in Rupees'])
data=data.groupby(['director','actor'])['tot nett gross in Rupees'].sum().reset_index()
data=data.sort_values('tot nett gross in Rupees',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','director','actor','tot nett gross in Rupees'])
data.to_csv('output-files/actor-director-highestgross.csv',index=False)


df=pd.read_csv('boxoffice_actors.csv')
mov=[k for k in df.movie_id]
mid=set(mov)
mid=list(mid)

fin=[]
for i in mid:
    dk=df[df['movie_id']==i]
    d=dk[dk['role']=='Director']
    direc=d['actor_name'].to_list()
    ng=d['nett_gross'].to_list()
    bgt=0
    if len(ng)!=0:
        bgt=ng[0]
        

    if len(direc)!=0:
        di=direc[0]
    else:
        di='na'
    
    a=dk[dk['role']=='Producer']
    actor=a['actor_name'].to_list()
    for j in actor:
        fin.append([di,j,bgt])
find=[]        
for i in range(len(fin)):
    if len(fin[i])>1:
        if fin[i][0]==fin[i][1]:
            find.append(fin[i])
            
for i in find:
    fin.remove(i)
    
data= pd.DataFrame(fin, columns = ['director','producer','tot nett gross in Rupees'])
data=data.groupby(['director','producer'])['tot nett gross in Rupees'].sum().reset_index()
data=data.sort_values('tot nett gross in Rupees',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','director','producer','tot nett gross in Rupees'])
data.to_csv('output-files/producer-director-highestgross.csv',index=False)



df=pd.read_csv('boxoffice_actors.csv')
mov=[k for k in df.movie_id]
mid=set(mov)
mid=list(mid)

fin=[]
for i in mid:
    dk=df[df['movie_id']==i]
    d=dk[dk['role']=='Lead Actor']
    direc=d['actor_name'].to_list()
    ng=d['nett_gross'].to_list()
    bgt=0
    if len(ng)!=0:
        bgt=ng[0]
        

    if len(direc)!=0:
        di=direc[0]
    else:
        di='na'
    
    a=dk[dk['role']=='Producer']
    actor=a['actor_name'].to_list()
    for j in actor:
        fin.append([di,j,bgt])
find=[]        
for i in range(len(fin)):
    if len(fin[i])>1:
        if fin[i][0]==fin[i][1]:
            find.append(fin[i])
            
for i in find:
    fin.remove(i)
    
data= pd.DataFrame(fin, columns = ['actor','producer','tot nett gross in Rupees'])
data=data.groupby(['actor','producer'])['tot nett gross in Rupees'].sum().reset_index()
data=data.sort_values('tot nett gross in Rupees',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','actor','producer','tot nett gross in Rupees'])
data.to_csv('output-files/producer-actor-highestgross.csv',index=False)




