#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Data for repository.csv', usecols = [1,12,13])
data['Ratio'] = data['Revenue(INR)'] / data['Budget(INR)']
n_data = data.loc[data['Release Period'] == 'Normal']
h_data = data.loc[data['Release Period'] == 'Holiday']
n_ratio = n_data['Ratio'].mean()
n_ratio
h_ratio = h_data['Ratio'].mean()
h_ratio
result = pd.DataFrame(columns = ['Release', 'Revenue-Budget Ratio'])
result.loc[0] = ['Normal', n_ratio]
result.loc[1] = ['Holiday', h_ratio]
ax = sns.barplot(x = result['Release'], y = result['Revenue-Budget Ratio'])
ax.set(xlabel = 'Release Day', ylabel = 'Revenue-Budget Ratio')
ax.set_title('Release day type vs Revenue-budget ratio')
plt.savefig('output-files/release-day-revenue-budget-ratio-graph.png')

data = pd.read_csv('Data for repository.csv', usecols = [5,12,13])
data['Ratio'] = data['Revenue(INR)'] / data['Budget(INR)']
n_data = data.loc[data['New Actor'] == 'Yes']
o_data = data.loc[data['New Actor'] == 'No']
n_ratio = n_data['Ratio'].mean()
n_ratio
o_ratio = o_data['Ratio'].mean()
o_ratio
result = pd.DataFrame(columns = ['Actor Status', 'Revenue-Budget Ratio'])
result.loc[0] = ['New', n_ratio]
result.loc[1] = ['Veteran', o_ratio]
ax = sns.barplot(x = result['Actor Status'], y = result['Revenue-Budget Ratio'])
ax.set(xlabel = 'Actor Status', ylabel = 'Revenue-Budget Ratio')
ax.set_title('Actor type vs Revenue-budget ratio')
plt.savefig('output-files/actor-type-revenue-budget-ratio-graph.png')

