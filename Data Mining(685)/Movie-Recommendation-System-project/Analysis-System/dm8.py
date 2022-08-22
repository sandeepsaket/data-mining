#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


data = pd.read_csv("Data for repository.csv", usecols = [4,8,9])
actor_data = pd.DataFrame(columns = ['Actor', 'Genre'])
a = list(sorted(set(data['Lead Star'])))
c = 0
for i in a:
    a_data = data.loc[data['Lead Star'] == i]
    c_dict = {}
    for j in a_data['Genre']:
        if i in c_dict.keys():
            c_dict[j] += 1
        else:
            c_dict[j] = 1
    m_genre = max(c_dict, key = c_dict.get)
    actor_data.loc[c] = [i, m_genre]
    c += 1

    
dir_data = pd.DataFrame(columns = ['Director', 'Genre'])
d = list(sorted(set(data['Director'])))
c = 0
for i in d:
    d_data = data.loc[data['Director'] == i]
    c_dict = {}
    for j in d_data['Genre']:
        if i in c_dict.keys():
            c_dict[j] += 1
        else:
            c_dict[j] = 1
    m_genre = max(c_dict, key = c_dict.get)
    dir_data.loc[c] = [i, m_genre]
    c += 1

actor_data.to_csv('output-files/actor-genre.csv', index = False)  
dir_data.to_csv('output-files/director-genre.csv', index = False)  

