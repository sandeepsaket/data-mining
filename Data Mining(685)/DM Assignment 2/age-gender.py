import pandas as pd
import numpy as np

df = pd.read_csv('Age and sex.csv')

df1 = pd.DataFrame()
df = (df[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2','Unnamed: 4','Unnamed: 6','Unnamed: 9','Unnamed: 10']][5:])
df[['Unnamed: 9','Unnamed: 10']] =  df[['Unnamed: 9','Unnamed: 10']].apply(pd.to_numeric)

for i in range(1,1081,30):
    df1 = (df1.append(df.iloc[i:8+i]))
df1.index = pd.RangeIndex(len(df1.index))

m = []
f = []
count = 0
for i in range(0,1080,30):
    k = count
    for j in range(k,k+8):
        m.append(((df1['Unnamed: 9'].iloc[j])/(df['Unnamed: 9'].iloc[i])))
        f.append(((df1['Unnamed: 10'].iloc[j])/(df['Unnamed: 10'].iloc[i])))
        count = count+1
     
df2 = pd.DataFrame(m,columns = ['male-ratio'])
df3 = pd.DataFrame(f,columns = ['female-ratio'])

c_df = pd.concat([df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2','Unnamed: 4']],df2,df3],axis=1)

n = 0
max_index_1 = []
max_index_2 = []
for x in range(0,36):
    c = n
    max_index_1.append(c_df['male-ratio'].iloc[c:c+8].idxmax())
    max_index_2.append(c_df['female-ratio'].iloc[c:c+8].idxmax())
    n = n+8

fdx_1 = pd.DataFrame()
fdx_2 = pd.DataFrame()
for a in range(0,len(max_index_1)):
    fdx_1 = fdx_1.append(c_df.iloc[max_index_1[a]])
    fdx_2 = fdx_2.append(c_df.iloc[max_index_2[a]])
fdx_1.index = pd.RangeIndex(len(fdx_1.index))
fdx_1 = fdx_1.rename(columns={'Unnamed: 4': 'age-group-males'})
fdx_2.index = pd.RangeIndex(len(fdx_2.index))
fdx_2 = fdx_2.rename(columns={'Unnamed: 4': 'age-group-females'})

c_df_1 = pd.concat([fdx_1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2']],fdx_1[['age-group-males','male-ratio']],fdx_2[['age-group-females','female-ratio']]],axis=1)
c_df_1 = c_df_1.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'States/UT Code','Unnamed: 2':'States/UT'})
print(" highest ratio of population that can speak 3 or more languages")
print(c_df_1)
c_df_1.to_csv('age-gender-a.csv')
del df1,df2,df3,c_df,fdx_1,fdx_2,c_df_1
max_index_1.clear()
max_index_2.clear()

## part 2
df = pd.read_csv('Age and sex.csv')
df1 = pd.DataFrame()
df = (df[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2','Unnamed: 4','Unnamed: 6','Unnamed: 7']][5:])
df[['Unnamed: 6','Unnamed: 7']] =  df[['Unnamed: 6','Unnamed: 7']].apply(pd.to_numeric)

for i in range(1,1081,30):
    df1 = (df1.append(df.iloc[i:8+i]))
df1.index = pd.RangeIndex(len(df1.index))

m = []
f = []
count = 0
for i in range(0,1080,30):
    k = count
    for j in range(k,k+8):
        m.append(((df1['Unnamed: 6'].iloc[j])/(df['Unnamed: 6'].iloc[i])))
        f.append(((df1['Unnamed: 7'].iloc[j])/(df['Unnamed: 7'].iloc[i])))
        count = count+1
     
df2 = pd.DataFrame(m,columns = ['male-ratio'])
df3 = pd.DataFrame(f,columns = ['female-ratio'])

c_df = pd.concat([df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2','Unnamed: 4']],df2,df3],axis=1)

n = 0
max_index_1 = []
max_index_2 = []
for x in range(0,36):
    c = n
    max_index_1.append(c_df['male-ratio'].iloc[c:c+8].idxmax())
    max_index_2.append(c_df['female-ratio'].iloc[c:c+8].idxmax())
    n = n+8

fdx_1 = pd.DataFrame()
fdx_2 = pd.DataFrame()
for a in range(0,len(max_index_1)):
    fdx_1 = fdx_1.append(c_df.iloc[max_index_1[a]])
    fdx_2 = fdx_2.append(c_df.iloc[max_index_2[a]])
fdx_1.index = pd.RangeIndex(len(fdx_1.index))
fdx_1 = fdx_1.rename(columns={'Unnamed: 4': 'age-group-males'})
fdx_2.index = pd.RangeIndex(len(fdx_2.index))
fdx_2 = fdx_2.rename(columns={'Unnamed: 4': 'age-group-females'})

c_df_1 = pd.concat([fdx_1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 2']],fdx_1[['age-group-males','male-ratio']],fdx_2[['age-group-females','female-ratio']]],axis=1)
c_df_1 = c_df_1.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'States/UT Code','Unnamed: 2':'States/UT'})
print(" highest ratio of population that can speak exactly 2 language ")
print(c_df_1)
c_df_1.to_csv('age-gender-b.csv')


    
