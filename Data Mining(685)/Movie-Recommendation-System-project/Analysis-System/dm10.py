#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv('bollywood_box_clean.csv')

#Most suucessful actor
dk=df.actors.str.split(',', expand=True)
df['act1'],df['act2'],df['act3']=dk[0],dk[1],dk[2]
dk=df.banner.str.split(',', expand=True)
df['ban1'],df['ban2'],df['ban3']=dk[0],dk[1],dk[2]
dk=df.producer.str.split(',', expand=True)
df['prod1'],df['prod2'],df['prod3']=dk[0],dk[1],dk[2]
dk=df.movie_director.str.split(',', expand=True)
df['dir']=dk[0]
df=df.filter(['movie_name','movie_total','movie_total_worldwide','act1','act2','act3','prod1','prod2','prod3','ban1','ban2','ban3','dir'])

actlist=df['act1'].to_list()
a2=df['act2'].to_list()
a3=df['act3'].to_list()
actlist.extend(a2)
actlist.extend(a3)
act = []
for i in actlist:
    if i not in act:
        act.append(i)
        
act.remove(None)
act.remove(np.nan)
        
prodlist=df['prod1'].to_list()
a2=df['prod2'].to_list()
a3=df['prod3'].to_list()
prodlist.extend(a2)
prodlist.extend(a3)
prod = []
for i in prodlist:
    if i not in prod:
        prod.append(i) 
        
prod.remove(None)
prod.remove(np.nan)        
        
banlist=df['ban1'].to_list()
a2=df['ban2'].to_list()
a3=df['ban3'].to_list()
banlist.extend(a2)
banlist.extend(a3)
ban = []
for i in banlist:
    if i not in ban:
        ban.append(i)        
ban.remove(None)


dirlist=df['dir'].to_list()
dirl = []
for i in dirlist:
    if i not in dirl:
        dirl.append(i)
        
dataset=[]
for i in act:
    dk=df[df["act1"]==i]
    dk1=df[df["act2"]==i]
    dk2=df[df["act3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['Actor', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
actor=dataset.iloc[0][0]
findata1=[]
findata1.append(['Most Successful Actor',actor])

dataset=[]
for i in ban:
    dk=df[df["ban1"]==i]
    dk1=df[df["ban2"]==i]
    dk2=df[df["ban3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['bannner', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
banner=dataset.iloc[0][0]
findata1.append(['Most Successful Banner',banner])


dataset=[]
for i in prod:
    dk=df[df["prod1"]==i]
    dk1=df[df["prod2"]==i]
    dk2=df[df["prod3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['producer', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
producer=dataset.iloc[0][0]
findata1.append(['Most Successful Producer',producer])

dataset=[]
for i in dirl:
    dk=df[df["dir"]==i]
    totcol=dk.movie_total.sum()
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['director', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
director=dataset.iloc[0][0]
findata1.append(['Most Successful Director',director])



dataset=[]
for i in act:
    dk=df[df["act1"]==i]
    dk1=df[df["act2"]==i]
    dk2=df[df["act3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total_worldwide.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['Actor', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
actor=dataset.iloc[0][0]
findata2=[]
findata2.append(['Most Successful Actor',actor])
dataset=[]
for i in ban:
    dk=df[df["ban1"]==i]
    dk1=df[df["ban2"]==i]
    dk2=df[df["ban3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total_worldwide.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['bannner', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
banner=dataset.iloc[0][0]
findata2.append(['Most Successful Banner',banner])


dataset=[]
for i in prod:
    dk=df[df["prod1"]==i]
    dk1=df[df["prod2"]==i]
    dk2=df[df["prod3"]==i]
    dk=pd.concat([dk,dk1,dk2])
    totcol=dk.movie_total_worldwide.sum()
    
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['producer', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
producer=dataset.iloc[0][0]
findata2.append(['Most Successful Producer',producer])

dataset=[]
for i in dirl:
    dk=df[df["dir"]==i]
    totcol=dk.movie_total_worldwide.sum()
    dataset.append([i,float(totcol)])
dataset = pd.DataFrame(dataset, columns = ['director', 'Total Earn'])
dataset=dataset.sort_values('Total Earn',ascending=False)
director=dataset.iloc[0][0]
findata2.append(['Most Successful Director',director])



df1 = pd.DataFrame(findata1, columns = ['Title(NET COLL. PAST 3 YEARS)', 'Holder'])

df2 = pd.DataFrame(findata2, columns = ['Title(WW COLL. PAST 3 YEARS)', 'Holder'])


df1.to_csv('output-files/net-mostsuccessful.csv', index = False)
df2.to_csv('output-files/worldwide-mostsuucessful.csv', index = False)

