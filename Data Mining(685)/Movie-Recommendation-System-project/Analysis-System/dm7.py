#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv('bollywood_full_1950-2019.csv')


dk=df.actors.str.split('|', expand=True)
df['act1'],df['act2'],df['act3'],df['act4'],df['act5'],df['act6'],df['act7'],df['act8'],df['act9'],df['act10'],df['act11'],df['act12'],df['act13'],df['act14'],df['act15']=dk[0],dk[1],dk[2],dk[3],dk[4],dk[5],dk[6],dk[7],dk[8],dk[9],dk[10],dk[11],dk[12],dk[13],dk[14]

actlist=df['act1'].to_list()
a2=df['act2'].to_list()
a3=df['act3'].to_list()
a4=df['act4'].to_list()
a5=df['act5'].to_list()
a6=df['act6'].to_list()
a7=df['act7'].to_list()
a8=df['act8'].to_list()
a9=df['act9'].to_list()
a10=df['act10'].to_list()
a11=df['act11'].to_list()
a12=df['act12'].to_list()
a13=df['act13'].to_list()
a14=df['act14'].to_list()
a15=df['act15'].to_list()



actlist.extend(a2)
actlist.extend(a3)
actlist.extend(a4)
actlist.extend(a5)
actlist.extend(a6)
actlist.extend(a7)
actlist.extend(a8)
actlist.extend(a9)
actlist.extend(a10)
actlist.extend(a11)
actlist.extend(a12)
actlist.extend(a13)
actlist.extend(a14)
actlist.extend(a15)








act = []
for i in actlist:
    if i not in act:
        act.append(i)
        
act.remove(None)
act.remove(np.nan)
act.remove('')



dataset=[]
for i in act:
    dk=df[df["act1"]==i]
    dk1=df[df["act2"]==i]
    dk2=df[df["act3"]==i]
    dk3=df[df["act4"]==i]
    dk4=df[df["act5"]==i]
    dk5=df[df["act6"]==i]
    dk6=df[df["act7"]==i]
    dk7=df[df["act8"]==i]
    dk8=df[df["act9"]==i]
    dk9=df[df["act10"]==i]
    dk10=df[df["act11"]==i]
    dk11=df[df["act12"]==i]
    dk12=df[df["act13"]==i]
    dk13=df[df["act14"]==i]
    dk14=df[df["act15"]==i]
    
    
    
    
    dk=pd.concat([dk,dk1,dk2,dk3,dk4,dk5,dk6,dk7,dk8,dk9,dk10,dk11,dk12,dk13,dk14])
    count=dk.count()
    count=count[0]
    avg=dk.imdb_rating.mean()
    high=dk.imdb_rating.max()
    
    dataset.append([i,count,high,round(avg,1)])
dataset = pd.DataFrame(dataset, columns = ['Actor', 'Number Of Movies','Highest Rating','Average Rating'])


dataset=dataset.sort_values('Number Of Movies',ascending=False)

dataset.to_csv('output-files/actor-movierating.csv', index = False)

df=pd.read_csv('bollywood_full_1950-2019.csv')
df1=pd.read_csv('bollywood_crew_data_1950-2019.csv')
df2=pd.read_csv('bollywood_crew_1950-2019.csv')

df2=df2.filter(['imdb_id','directors'])
df1=df1.filter(['crew_id','name'])
df1.columns=['directors','name']

df1= pd.merge(df1, df2, how ='inner', on =['directors'])

df1=df1.filter(['name','imdb_id'])
df1.columns=['directors','imdb_id']

dff= pd.merge(df, df1, how ='inner', on =['imdb_id'])


dlist=dff['directors'].to_list()
dire = []
for i in dlist:
    if i not in dire:
        dire.append(i)
        


dataset=[]
for i in dire:
    dk=dff[dff["directors"]==i]
    count=dk.count()
    count=count[0]
    avg=dk.imdb_rating.mean()
    high=dk.imdb_rating.max()
    
    dataset.append([i,count,high,round(avg,1)])
dataset = pd.DataFrame(dataset, columns = ['Director', 'Number Of Movies','Highest Rating','Average Rating'])


dataset=dataset.sort_values('Number Of Movies',ascending=False)

dataset.to_csv('output-files/director-movierating.csv', index = False)

