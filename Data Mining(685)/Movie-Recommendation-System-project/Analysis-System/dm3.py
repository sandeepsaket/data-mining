#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv('bollywood_full_1950-2019.csv')[['title_x','imdb_id','genres','imdb_rating','imdb_votes','summary','actors','year_of_release']]

genres = []
genr_data = {}
for m in np.array(movies[['imdb_votes','genres','year_of_release']]):
    gens = str(m[1]).split('|')
    votes = m[0]
    year = m[2]
    try:votes = int(votes)
    except:votes = 0
    
    if(year.isnumeric()):
        if(year in genr_data):
            dict_f = genr_data[year]
            for g in gens:
                genres.append(g)
                if (g.title() in dict_f):
                    dv = dict_f[g.title()]
                    dv += votes
                    dict_f[g.title()] = dv
                else:
                    dict_f[g.title()] = votes
            dict_f = dict(sorted(dict_f.items(),reverse=True,key= lambda e: e[1]))
            genr_data[year] = dict_f

        else:
            dict_f = {}
            for g in gens:
                genres.append(g)
                dict_f[g.title()] = votes
            dict_f = dict(sorted(dict_f.items(),reverse=True,key= lambda e: e[1]))
            genr_data[year] = dict_f
            
genr_data = dict(sorted(genr_data.items()))

result = pd.DataFrame(columns = ['Year', 'Gnere 1', 'Gnere 2', 'Gnere 3', 'Gnere 4', 'Gnere 5'])
c = 0
for y in genr_data:
    df = list(genr_data[y].keys())[:5]
    s = list()
    for g in df:
        s.append(g)
    result.loc[c] = [y, s[0], s[1], s[2], s[3], s[4]]
    c += 1
result.to_csv("output-files/most-used-genre.csv", index = False)

data = pd.read_csv("boxoffice_movies.csv", usecols = [2,11])
data.dropna(inplace = True)
data.sort_values('release_date', inplace = True)
data.reset_index(inplace = True, drop = True)

n_data = pd.DataFrame(columns = ['Year', 'Collection'])
for i in range(0, len(data['release_date'])):
    n_data.loc[i] = [str(data['release_date'].loc[i]).split('-')[0], data['adjusted_nett_gross'].loc[i]]
f_data = pd.DataFrame(columns = ['Year', 'No. of Movies', 'Total Collection', 'Avg. Collection'])
c = 0
year_list = list(sorted(set(n_data['Year'])))
for i in year_list:
    y_data = n_data.loc[n_data['Year'] == i]
    l = len(y_data['Year'])
    tot = y_data['Collection'].sum()
    f_data.loc[c] = [i, l, tot, (tot / l)]
    c += 1

f_data = f_data.loc[2:]
plt.figure(figsize=[30,15])
plt.plot(f_data['Year'], f_data['Avg. Collection'])
plt.xlabel('Year')
plt.ylabel('Average Collection in 10 Crores')
plt.title('Comparision of average collection of movies to the release year')
plt.savefig('output-files/year-collection-graph.png')
f_data.to_csv('output-files/year-collection.csv', index = False)


