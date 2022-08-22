#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

crew = pd.read_csv('boxoffice_actors.csv')
movies = pd.read_csv('bollywood_movies.csv')

df = pd.merge(crew, movies, on='imdb_id')[['actor_id', 'actor_name', 'role', 'imdb_id', 'nett_gross', 'rating', 'votes']].copy()

df = df.loc[df['rating'] != '-']

df['rating'] = df['rating'].astype(float)

actors = df.loc[df['role'] == 'Lead Actor'].copy()

directors = df.loc[df['role'] == 'Director'].copy()

actors = actors.join(actors.groupby('actor_id')['rating'].mean(), on='actor_id', rsuffix='_mean')

actors = actors.join(actors.groupby('actor_id')['nett_gross'].sum(), on='actor_id', rsuffix='_sum')

actors = actors.join(actors.groupby('actor_id')['role'].count(), on='actor_id', rsuffix='_count')

actors = actors.loc[actors['role_count'] > 3]

min_rating = actors['rating_mean'].min()
max_rating = actors['rating_mean'].max()

actors['normalized_rating'] = (actors['rating_mean'] - min_rating) / (max_rating - min_rating)

min_gross = actors['nett_gross_sum'].min()
max_gross = actors['nett_gross_sum'].max()

actors['normalized_gross'] = (actors['nett_gross_sum'] - min_gross) / (max_gross - min_gross)

actors['Score'] = (actors['normalized_gross'] + actors['normalized_rating']) / 2

max_s = actors['Score'].max()
min_s = actors['Score'].min()
actors['Score'] = ((actors['Score'] - min_s) / (max_s - min_s)) * 10

top_actors = actors.sort_values('Score', ascending=False).drop_duplicates(subset=['actor_id'])[:100][['actor_name', 'Score']]

top_actors.to_csv('output-files/actor-score.csv', index=False)
    
    
directors = directors.join(directors.groupby('actor_id')['rating'].mean(), on='actor_id', rsuffix='_mean')

directors = directors.join(directors.groupby('actor_id')['nett_gross'].sum(), on='actor_id', rsuffix='_mean')

directors = directors.join(directors.groupby('actor_id')['role'].count(), on='actor_id', rsuffix='_count')

directors = directors.loc[directors['role_count'] > 3]

min_rating = directors['rating_mean'].min()
max_rating = directors['rating_mean'].max()

directors['normalized_rating'] = (directors['rating_mean'] - min_rating) / (max_rating - min_rating)

min_gross = directors['nett_gross_mean'].min()
max_gross = directors['nett_gross_mean'].max()

directors['normalized_gross'] = (directors['nett_gross_mean'] - min_gross) / (max_gross - min_gross)

min_rating = directors['role_count'].min()
max_rating = directors['role_count'].max()

directors['normalized_count'] = (directors['role_count'] - min_rating) / (max_rating - min_rating)

directors['Score'] = (directors['normalized_gross'] + directors['normalized_rating']) / 2
max_s = directors['Score'].max()
min_s = directors['Score'].min()
directors['Score'] = ((directors['Score'] - min_s) / (max_s - min_s)) * 10


directors = directors.rename(columns={'actor_name': 'director_name'})
top_directors = directors.sort_values('Score', ascending=False).drop_duplicates(subset=['actor_id'])[:100][['director_name', 'Score']]

top_directors.to_csv('output-files/director-score.csv', index=False)

