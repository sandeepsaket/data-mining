#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
df=pd.read_csv('boxoffice.csv')

mov=[k for k in df.movie_id]
mid=set(mov)
mid=list(mid)
c100=0
c200=0
c300=0
data=[]
for i in mid:
    dk=df[df['movie_id']==i]
    l=dk.total_nett_gross.to_list()
    if len(l)==1:
        if l[0]>1000000000 and l[0]<2000000000:
            c100=c100+1
        if l[0]>2000000000 and l[0]<3000000000:
            c200=c200+1 
        if l[0]>3000000000:
            c300=c300+1
data.append(['Total Movies',c100,c200,c300])
df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Lead Actor']
mov=[k for k in df.actor_name]
mid=set(mov)
mid=list(mid)
c1=0
c2=0
c3=0
a=''
b=''
c=''
for i in mid:
    dk=df[df['actor_name']==i]
    c100=0
    c200=0
    c300=0
    l=dk.nett_gross.to_list()
    for j in range(len(l)):
        
        if l[j]>1000000000 and l[j]<2000000000:
            c100=c100+1
        if l[j]>2000000000 and l[j]<3000000000:
            c200=c200+1 
        if l[j]>3000000000:
            c300=c300+1
    if c100>c1:
        c1=c100
        a=i
    if c200>c2:
        c2=c200
        b=i
    if c300>c3:
        c3=c300
        c=i
data.append(['Actors With Most Movies',a+'('+str(c1)+')',b+'('+str(c2)+')',c+'('+str(c3)+')'])

df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Director']
mov=[k for k in df.actor_name]
mid=set(mov)
mid=list(mid)
c1=0
c2=0
c3=0
a=''
b=''
c=''
for i in mid:
    dk=df[df['actor_name']==i]
    c100=0
    c200=0
    c300=0
    l=dk.nett_gross.to_list()
    for j in range(len(l)):
        
        if l[j]>1000000000 and l[j]<2000000000:
            c100=c100+1
        if l[j]>2000000000 and l[j]<3000000000:
            c200=c200+1 
        if l[j]>3000000000:
            c300=c300+1
    if c100>c1:
        c1=c100
        a=i
    if c200>c2:
        c2=c200
        b=i
    if c300>c3:
        c3=c300
        c=i
data.append(['Directors With Most Movies',a+'('+str(c1)+')',b+'('+str(c2)+')',c+'('+str(c3)+')'])

df=pd.read_csv('boxoffice_actors.csv')
df=df[df['role']=='Producer']
mov=[k for k in df.actor_name]
mid=set(mov)
mid=list(mid)
c1=0
c2=0
c3=0
a=''
b=''
c=''
for i in mid:
    dk=df[df['actor_name']==i]
    c100=0
    c200=0
    c300=0
    l=dk.nett_gross.to_list()
    for j in range(len(l)):
        
        if l[j]>1000000000 and l[j]<2000000000:
            c100=c100+1
        if l[j]>2000000000 and l[j]<3000000000:
            c200=c200+1 
        if l[j]>3000000000:
            c300=c300+1
    if c100>c1:
        c1=c100
        a=i
    if c200>c2:
        c2=c200
        b=i
    if c300>c3:
        c3=c300
        c=i
data.append(['Producers With Most Movies',a+'('+str(c1)+')',b+'('+str(c2)+')',c+'('+str(c3)+')'])

data=pd.DataFrame(data,columns=['Title','100 CR CLUB','200 CR CLUB','300 CR CLUB'])
data=data.set_index('Title')
data.to_csv('output-files/movies-clubs.csv',index=False)
df=pd.read_csv('boxoffice_actors.csv')
df1=pd.read_csv('boxoffice.csv')

df=df[df['role']=='Lead Actor']
df = pd.merge(df, df1, how="inner", on=["movie_id"])         
act=[k for k in df.actor_name]
actor=set(act)
actor=list(actor)   
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    ff=dj['footfalls'].sum()
    data.append([i,ff])
data=pd.DataFrame(data,columns=['Actor','Cummulative Footfalls(of all movies)'])
data=data.sort_values('Cummulative Footfalls(of all movies)',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','Actor','Cummulative Footfalls(of all movies)'])
data.to_csv('output-files/topactors-footfalls.csv',index=False)


df=pd.read_csv('boxoffice_actors.csv')
df1=pd.read_csv('boxoffice.csv')

df=df[df['role']=='Director']
df = pd.merge(df, df1, how="inner", on=["movie_id"])         
act=[k for k in df.actor_name]
actor=set(act)
actor=list(actor)   
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    ff=dj['footfalls'].sum()
    data.append([i,ff])
data=pd.DataFrame(data,columns=['Director','Cummulative Footfalls(of all movies)'])
data=data.sort_values('Cummulative Footfalls(of all movies)',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','Director','Cummulative Footfalls(of all movies)'])
data.to_csv('output-files/topdirectors-footfalls.csv',index=False)

df=pd.read_csv('boxoffice_actors.csv')
df1=pd.read_csv('boxoffice.csv')

df=df[df['role']=='Producer']
df = pd.merge(df, df1, how="inner", on=["movie_id"])         
act=[k for k in df.actor_name]
actor=set(act)
actor=list(actor)   
data=[]
for i in actor:
    dj=df[df['actor_name']==i]
    ff=dj['footfalls'].sum()
    data.append([i,ff])
data=pd.DataFrame(data,columns=['Producer','Cummulative Footfalls(of all movies)'])
data=data.sort_values('Cummulative Footfalls(of all movies)',ascending=False)
data=data.head(20)
data=data.reset_index(drop=True)
data['rank']=data.index+1
data=data.filter(['rank','Producer','Cummulative Footfalls(of all movies)'])
data.to_csv('output-files/topproducers-footfalls.csv',index=False)




