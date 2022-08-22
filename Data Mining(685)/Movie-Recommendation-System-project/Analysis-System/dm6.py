#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Data for repository.csv')

df=df.filter(['Movie Name','Number of Screens','Revenue(INR)','Budget(INR)','Genre'])
df.columns=['Movie Name','Number of Screens','Budget(INR) + Promotions','Gross Collections','Genre']

df['Profit Made through Box office']=df['Gross Collections']-df['Budget(INR) + Promotions']
df['Profit Percentage']=df['Profit Made through Box office']*100/df['Budget(INR) + Promotions']
df=df.sort_values('Profit Percentage',ascending=False)

df.index = np.arange(1, len(df) + 1)
df['Rankings'] = df.index



dfd=df.sort_values('Number of Screens') 
# x axis values
x = np.array(dfd['Number of Screens'].to_list())
# corresponding y axis values
y = dfd['Gross Collections'].to_list()
plt.figure(figsize=(16,10))
 
# plotting the points
plt.plot(x, y)
 
plt.xlabel('Number of screens')
plt.ylabel('Gross Collection in hundred crores')
plt.xlim(100,4000)
 
# giving a title to my graph
plt.title('Significance Of Screens Count for a Movies Collection')
 
# function to show the plot
plt.savefig('output-files/screen-gross-graph.png')



gen=df['Genre'].to_list()
genre = []
for i in gen:
    if i not in genre:
        genre.append(i)
        
dataset=[]
for i in genre:
    dk=df[df["Genre"]==i]
    count=dk.count()
    totgross=pd.to_numeric(dk["Gross Collections"]).sum()
    totprof=pd.to_numeric(dk["Profit Made through Box office"]).sum()
    
    meanprof= pd.to_numeric(dk["Profit Made through Box office"]).mean()
    meanprof=int(meanprof)
    meang=pd.to_numeric(dk["Gross Collections"]).mean()
    meang=int(meang)
    
    dataset.append([i,count[0],totgross,totprof,meanprof,meang])
    
dataset = pd.DataFrame(dataset, columns = ['Genre', 'Number of Movies','Total Gross Collection From the genre','Total Profit From the Genre','Mean Profit (per movie From the genre)','Mean Gross Collection (per movie From the genre)'])

dfa1=dataset.sort_values('Number of Movies',ascending=False)
dfa1.index = np.arange(1, len(dfa1) + 1)
dfa1['Rankings'] = dfa1.index
dfa1=dfa1.filter(['Rankings','Genre','Number of Movies'])


dfa2=dataset.sort_values('Total Profit From the Genre',ascending=False)
dfa2.index = np.arange(1, len(dfa2) + 1)
dfa2['Rankings'] = dfa2.index
dfa2=dfa2.filter(['Rankings','Genre','Total Profit From the Genre'])

dfa3=dataset.sort_values('Total Gross Collection From the genre',ascending=False)
dfa3.index = np.arange(1, len(dfa3) + 1)
dfa3['Rankings'] = dfa3.index
dfa3=dfa3.filter(['Rankings','Genre','Total Gross Collection From the genre'])

dfa4=dataset.sort_values('Mean Profit (per movie From the genre)',ascending=False)
dfa4.index = np.arange(1, len(dfa4) + 1)
dfa4['Rankings'] = dfa4.index
dfa4=dfa4.filter(['Rankings','Genre','Mean Profit (per movie From the genre)'])

dfa5=dataset.sort_values('Mean Gross Collection (per movie From the genre)',ascending=False)
dfa5.index = np.arange(1, len(dfa5) + 1)
dfa5['Rankings'] = dfa5.index
dfa5=dfa5.filter(['Rankings','Genre','Mean Gross Collection (per movie From the genre)'])


dfa1.to_csv('output-files/genre-ranking-popular.csv', index = False)
dfa2.to_csv('output-files/genre-ranking-total-profit.csv', index = False)
dfa3.to_csv('output-files/genre-ranking-total-gross.csv', index = False)
dfa4.to_csv('output-files/genre-ranking-average-profit.csv', index = False)
dfa5.to_csv('output-files/genre-ranking-average-gross.csv', index = False)

