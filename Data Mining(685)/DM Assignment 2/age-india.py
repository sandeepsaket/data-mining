import pandas as pd
import numpy as np

df = pd.read_csv('Age and sex.csv')

df = df[['Unnamed: 2','Unnamed: 4','Unnamed: 8']]


df['Unnamed: 8'].iloc[5:] = df['Unnamed: 8'].iloc[5:].apply(pd.to_numeric)

df1 = pd.DataFrame()


for i in range (0,1056,30):
    df1 = (df1.append(df.iloc[6+i:14+i]))

df1['Unnamed: 8'] = df1['Unnamed: 8'].apply(pd.to_numeric)
df1.index = pd.RangeIndex(len(df1.index))


f = []
count = 0
for i in range(5,1060,30):
    k = count
    for j in range(k,k+8):
        f.append(((df1['Unnamed: 8'].iloc[j])/(df['Unnamed: 8'].iloc[i]))*100)
        count = count+1

df2 = pd.DataFrame(f,columns = ['percentage'])


c_df = pd.concat([df1[['Unnamed: 2','Unnamed: 4']],df2],axis=1)
c_df = c_df.rename(columns={'Unnamed: 2':'States/UT','Unnamed: 4':'age-Group','percentage':'percentage'})

n = 0
max_index = []
for x in range(0,36):
    c = n
    max_index.append(c_df['percentage'].iloc[c:c+8].idxmax())
    n = n+8

fdx = pd.DataFrame()
for a in range(0,len(max_index)):
    fdx = fdx.append(c_df.iloc[max_index[a]])
print(fdx)

fdx.to_csv('age-india.csv')







