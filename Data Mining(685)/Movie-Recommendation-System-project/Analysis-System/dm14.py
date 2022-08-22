#!/usr/bin/env python
# coding: utf-8





import pandas as pd
import numpy as np


data = pd.read_csv('boxoffice_movies.csv', usecols = [2,3])
data.dropna(inplace = True)
data.sort_values('release_date', inplace = True)
data.reset_index(inplace = True, drop = True)
f_data = pd.DataFrame(columns = ['Year', 'Month', 'Collection'])
for i in range(0, len(data['release_date'])):
    y = str(data['release_date'].loc[i]).split('-')[0]
    m = str(data['release_date'].loc[i]).split('-')[1]
    f_data.loc[i] = [y, m, data['total_nett_gross'].loc[i]]
result = pd.DataFrame(columns = ['Year', 'Month', 'Total Collection'])
c = 0
year_list = list(sorted(set(f_data['Year'])))

for i in year_list:
    y_data = f_data.loc[f_data['Year'] == i]
    tot_c = y_data.groupby('Month').sum()
    tot_c.reset_index(inplace = True)
    max_c = max(tot_c['Collection'])
    result.loc[c] = [i, int(tot_c['Month'].loc[tot_c['Collection'] == max_c]), max_c]
    c += 1
result = result.loc[2:]

m_dict = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May', 6 : 'Jun', 7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
a = list()
for i in result['Month']:
    a.append(m_dict[i])
result['Month'] = a
result.to_csv('output-files/month-total-collection.csv', index = False)

data = pd.read_csv('boxoffice_movies.csv', usecols = [2,10])
data.dropna(inplace = True)
data.sort_values('release_date', inplace = True)
data.reset_index(inplace = True, drop = True)

f_data = pd.DataFrame(columns = ['Year', 'Month', 'Footfalls'])
for i in range(0, len(data['release_date'])):
    y = str(data['release_date'].loc[i]).split('-')[0]
    m = str(data['release_date'].loc[i]).split('-')[1]
    f_data.loc[i] = [y, m, data['footfalls'].loc[i]]
result = pd.DataFrame(columns = ['Year', 'Month', 'Footfalls'])
c = 0
year_list = list(sorted(set(f_data['Year'])))
for i in year_list:
    y_data = f_data.loc[f_data['Year'] == i]
    tot_c = y_data.groupby('Month').sum()
    tot_c.reset_index(inplace = True)
    max_c = max(tot_c['Footfalls'])
    result.loc[c] = [i, int(tot_c['Month'].loc[tot_c['Footfalls'] == max_c]), max_c]
    c += 1
result = result.loc[2:]

m_dict = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May', 6 : 'Jun', 7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
a = list()
for i in result['Month']:
    a.append(m_dict[i])
result['Month'] = a
result.to_csv('output-files/month-footfalls.csv', index = False)

