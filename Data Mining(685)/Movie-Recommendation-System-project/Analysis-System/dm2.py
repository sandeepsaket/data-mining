#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

c_data = pd.read_csv("Data for repository.csv", usecols = [4,12])
c_data.dropna(inplace = True)
c_data.reset_index(inplace = True, drop = True)
genre_dict = {}
for i in range(0, len(c_data['Genre'])):
        a = c_data['Genre'].loc[i]
        if a in genre_dict.keys():
            genre_dict[a] += c_data['Revenue(INR)'].loc[i]
        else:
            genre_dict[a] = c_data['Revenue(INR)'].loc[i]
g_data = pd.DataFrame(genre_dict.items(), columns=['Genre', 'Collection'])
g_data.sort_values('Collection', inplace = True)
g_data.to_csv('output-files/genre-collection.csv')
plt.figure(figsize=(20, 10), dpi=80)
ax = sns.barplot(x = g_data['Genre'], y = g_data['Collection'])
ax.set(xlabel = 'Genre', ylabel = 'Collection in 1000 Crores INR')
ax.set_title("Comparision of collection done by various Genres for the past 13 years")
plt.savefig('output-files/genre-collection-graph.png')

r_data = pd.read_csv("bollywood_full_1950-2019.csv", usecols = [1,5,10])
r_data.rename(columns = {'original_title' : 'name'}, inplace = True)
c_data = pd.read_csv("boxoffice.csv", usecols = [1,11,12])
c_data.rename(columns = {'adjusted_nett_gross' : 'collection'}, inplace = True)
f_data = r_data.merge(c_data, on = 'imdb_id', how = 'inner')
f_data.drop(['name_y', 'imdb_id'], axis = 1, inplace = True)
f_data.rename(columns = {'name_x' : 'Movie Name'}, inplace = True)
f_data.sort_values('imdb_rating', inplace = True)
f_data.to_csv('output-files/rating-collection.csv')
plt.figure(figsize = (20, 10))
plt.plot(f_data['imdb_rating'], f_data['collection'])
plt.xlabel('Ratings of movies')
plt.ylabel('Colection in 100 Crores INR')
plt.title('Comparision of collection and rating of bollywood movies')
plt.savefig('output-files/rating-collection-graph.png')

