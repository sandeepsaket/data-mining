#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


actor_data = pd.read_csv('BollywoodActorRanking.csv')
director_data = pd.read_csv('BollywoodDirectorRanking.csv')

names = actor_data['actorName']
hits_and_rating = actor_data[['googleHits','normalizedRating']]
hits_and_rating = (hits_and_rating - hits_and_rating.min())*10/(hits_and_rating.max() - hits_and_rating.min())
actor_df = pd.concat([names,hits_and_rating],axis=1)
actor_df = actor_df.nlargest(10,'googleHits')
actor_df.reset_index(inplace = True, drop=True)
actor_df.to_csv('output-files/popular-actor.csv')

X = actor_df['actorName']
X_axis = np.arange(len(X)) 
y1_axis = actor_df['googleHits']
y2_axis = actor_df['normalizedRating']
plt.figure(figsize=[15,7])
plt.bar(X_axis - 0.2, y1_axis, 0.4, label='Google Hits')
plt.bar(X_axis + 0.2, y2_axis, 0.4, label='Rating')
plt.legend()
plt.xticks(X_axis,X,rotation=30)
plt.savefig('output-files/popular-actor-graph.png')

names = director_data['directorName']
hits_and_rating = director_data[['googleHits','normalizedRating']]
hits_and_rating = (hits_and_rating - hits_and_rating.min())*10/(hits_and_rating.max() - hits_and_rating.min())
director_df = pd.concat([names,hits_and_rating],axis=1)
director_df = director_df.nlargest(10,'googleHits')
director_df.reset_index(inplace = True, drop=True)
director_df.to_csv('output-files/popular-director.csv')

X = director_df['directorName']
X_axis = np.arange(len(X)) 
y1_axis = director_df['googleHits']
y2_axis = director_df['normalizedRating']
plt.figure(figsize=[15,7])
plt.bar(X_axis - 0.2, y1_axis, 0.4, label='Google Hits')
plt.bar(X_axis + 0.2, y2_axis, 0.4, label='Rating')
plt.legend()
plt.xticks(X_axis,X,rotation=30)
plt.savefig('output-files/popular-director-graph.png')

names = actor_data['actorName']
count_and_rating = actor_data[['movieCount','normalizedRating']]
actor_df = pd.concat([names,count_and_rating],axis=1)
actor_df = actor_df.nlargest(10,'movieCount')
actor_df.reset_index(inplace = True, drop=True)
actor_df.to_csv('output-files/maximum-movies-actor.csv')

X = actor_df['actorName']
X_axis = np.arange(len(X)) 
y1_axis = actor_df['movieCount']
y2_axis = actor_df['normalizedRating']
plt.figure(figsize=[15,7])
plt.bar(X_axis - 0.2, y1_axis, 0.4, label='No. of Movies')
plt.bar(X_axis + 0.2, y2_axis, 0.4, label='Rating')
plt.legend()
plt.xticks(X_axis,X,rotation=30)
plt.savefig('output-files/maximum-movies-actor-graph.png')


names = director_data['directorName']
hits_and_rating = director_data[['movieCount','normalizedRating']]
director_df = pd.concat([names,hits_and_rating],axis=1)
director_df = director_df.nlargest(10,'movieCount')
director_df.reset_index(inplace = True, drop=True)
director_df.to_csv('output-files/maximum-movies-director.csv')


X = director_df['directorName']
X_axis = np.arange(len(X)) 
y1_axis = director_df['movieCount']
y2_axis = director_df['normalizedRating']
plt.figure(figsize=[15,7])
plt.bar(X_axis - 0.2, y1_axis, 0.4, label='No. of Movies')
plt.bar(X_axis + 0.2, y2_axis, 0.4, label='Rating')
plt.legend()
plt.xticks(X_axis,X,rotation=30)
plt.savefig('output-files/maximum-movies-director-graph.png')





