#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

r_data = pd.read_csv("bollywood_full_1950-2019.csv", usecols = [1,5,10])
c_data = pd.read_csv("boxoffice.csv", usecols = [1,11,12])
r_data.rename(columns = {'imdb_id' : 'imdb_id', 'original_title' : 'name', 'imdb_rating' : 'imdb_rating'}, inplace = True)
c_data.rename(columns = {'name' : 'name', 'adjusted_nett_gross' : 'Revenue', 'imdb_id' : 'imdb_id'}, inplace = True)
f_data = r_data.merge(c_data, on = 'imdb_id', how = 'inner')
max_r = f_data['Revenue'].max()
min_r = f_data['Revenue'].min()
f_data['Score'] = (f_data['imdb_rating'] * 0.5) + (((f_data['Revenue'] - min_r) / (max_r - min_r)) * 10)
f_data.sort_values('Score', ascending=False, inplace = True)
f_data.reset_index(inplace = True, drop = True)
max_s = f_data['Score'].max()
min_s = f_data['Score'].min()
f_data['Score'] = ((f_data['Score'] - min_s) / (max_s - min_s)) * 10
f_data.drop(['imdb_id', 'name_y'], axis = 1, inplace = True)
f_data.rename(columns = {'name_x' : 'Movie Name'}, inplace = True)
f_data.to_csv('output-files/movie-score.csv', index = False)

