#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
df1=pd.read_csv('boxoffice_actors.csv')
df1=df1[df1['role']=='Lead Actor']
act=[k for k in df1.actor_name]
actor=set(act)
data=[]
for i in actor:
    dk=df1[df1['actor_name']==i]
    nett=dk['nett_gross'].sum()
    data.append([i,nett])
data = pd.DataFrame(data, columns = ['actor','total nett gross']) 
data=data.sort_values('total nett gross',ascending=False)
data.index = np.arange(1, len(data) + 1)
data['rank'] = data.index
data=data.head(20)
data=data.filter(['rank','actor','total nett gross'])
data.columns=['rank','actor','Total India Collection of all their movies in Rupees']
    
data.to_csv('output-files/top20-actor-highestcoll.csv',index=False)

df1=pd.read_csv('boxoffice_actors.csv')
df1=df1[df1['role']=='Director']
act=[k for k in df1.actor_name]
actor=set(act)
data=[]
for i in actor:
    dk=df1[df1['actor_name']==i]
    nett=dk['nett_gross'].sum()
    data.append([i,nett])
data = pd.DataFrame(data, columns = ['actor','total nett gross']) 
data=data.sort_values('total nett gross',ascending=False)
data.index = np.arange(1, len(data) + 1)
data['rank'] = data.index
data=data.head(20)
data=data.filter(['rank','actor','total nett gross'])
data.columns=['rank','director','Total India Collection of all their movies in Rupees']
    
data.to_csv('output-files/top20-director-highestcoll.csv',index=False)


df1=pd.read_csv('boxoffice_actors.csv')
df1=df1[df1['role']=='Producer']
act=[k for k in df1.actor_name]
actor=set(act)
data=[]
for i in actor:
    dk=df1[df1['actor_name']==i]
    nett=dk['nett_gross'].sum()
    data.append([i,nett])
data = pd.DataFrame(data, columns = ['actor','total nett gross']) 
data=data.sort_values('total nett gross',ascending=False)
data.index = np.arange(1, len(data) + 1)
data['rank'] = data.index
data=data.head(20)
data=data.filter(['rank','actor','total nett gross'])
data.columns=['rank','producer','Total India Collection of all their movies in Rupees']
    
data.to_csv('output-files/top20-producer-highestcoll.csv',index=False)





