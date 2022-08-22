#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


f_data = pd.DataFrame(columns = ['Movie Name'])
data = pd.read_csv("boxoffice.csv")
f_data['Movie Name'] = data['name']
f_data['India Collection'] = data['india_gross']
f_data['Overseas Collection'] = data['overseas_gross']
f_data['Worldwide Collection'] = data['worldwide_gross']
f_data['Opening Week Percent'] = (data['first_week'] / f_data['Worldwide Collection']) * 100
f_data['Overseas Percent'] = (f_data['Overseas Collection'] / f_data['Worldwide Collection']) * 100
f_data = f_data.replace([np.inf, -np.inf, 0], np.nan).dropna(axis=0)
f_data.sort_values('Overseas Percent', ascending = False, inplace = True)
f_data.to_csv('output-files/collection-india-worldwide.csv', index = False)

