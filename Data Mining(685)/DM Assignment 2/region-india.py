import numpy as np
import pandas as pd

f = pd.DataFrame()
f1 = pd.read_csv("Jammu & Kashmir.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Punjab.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Himanchal Pradesh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Haryana.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Uttarakhand.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("NCT of Delhi.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Chandigarh UT.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])
north = f.sort_values(by = ['Unnamed: 4'],ascending = False)
north = north.reset_index(drop=True)

del f

df_new = north[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
north_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
north_new = north_new.reset_index(drop=True)




f = pd.DataFrame()
f1 = pd.read_csv("Rajasthan.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Gujrat.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Maharashtra.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Goa.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Daman & Diu UT.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])
west = f.sort_values(by = ['Unnamed: 4'],ascending = False)

west = west.reset_index(drop=True)

del f

df_new = west[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
west_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
west_new = west_new.reset_index(drop=True)



f = pd.DataFrame()
f1 = pd.read_csv("Madhaya Pradesh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Uttar Pradesh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Chattishgarh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])

central = f.sort_values(by = ['Unnamed: 4'],ascending = False)

central = central.reset_index(drop=True)

del f

df_new = central[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
central_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
central_new = central_new.reset_index(drop=True)



f = pd.DataFrame()
f1 = pd.read_csv("Bihar.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("West Bengal.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Odisha.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Jharkhand.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])

east = f.sort_values(by = ['Unnamed: 4'],ascending = False)

east = east.reset_index(drop=True)

del f

df_new = east[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
east_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
east_new = east_new.reset_index(drop=True)



f = pd.DataFrame()
f1 = pd.read_csv("Karnataka.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])



f1 = pd.read_csv("Andra Pradesh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Tamil Nadu.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Kerala.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Lakhadweep.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Paducherry UT.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])
south = f.sort_values(by = ['Unnamed: 4'],ascending = False)
south = south.reset_index(drop=True)

del f

df_new = south[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
south_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
south_new = south_new.reset_index(drop=True)



f = pd.DataFrame()
f1 = pd.read_csv("Assam.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Sikkim.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Meghalaya.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Tripura.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Arunachal Pradesh.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Manipur.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Nagaland.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Mizoram.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])


f1 = pd.read_csv("Andaman nikobar.csv")

f2 = (f1[['Unnamed: 1','Unnamed: 3','Unnamed: 4']])

f3 = f2.dropna()
f3 = f3.astype({'Unnamed: 4':'float64'})

f = f.append(f3.iloc[1:])

north_east = f.sort_values(by = ['Unnamed: 4'],ascending = False)
north_east = north_east.reset_index(drop=True)

del f


df_new = north_east[['Unnamed: 3','Unnamed: 4']].groupby(['Unnamed: 3']).agg({'Unnamed: 4': 'sum'}).reset_index()
north_east_new = df_new.sort_values(by = ['Unnamed: 4'],ascending = False)
north_east_new = north_east_new.reset_index(drop=True)



data = {'Region': ['North', 'West', 'Central', 'East','South','North-East'], 'Language-1': [north_new['Unnamed: 3'].iloc[0],west_new['Unnamed: 3'].iloc[0],central_new['Unnamed: 3'].iloc[0],east_new['Unnamed: 3'].iloc[0],south_new['Unnamed: 3'].iloc[0],north_east_new['Unnamed: 3'].iloc[0]],'Language-2': [north_new['Unnamed: 3'].iloc[1],west_new['Unnamed: 3'].iloc[1],central_new['Unnamed: 3'].iloc[1],east_new['Unnamed: 3'].iloc[1],south_new['Unnamed: 3'].iloc[1],north_east_new['Unnamed: 3'].iloc[1]],'Language-3':[north_new['Unnamed: 3'].iloc[2],west_new['Unnamed: 3'].iloc[2],central_new['Unnamed: 3'].iloc[2],east_new['Unnamed: 3'].iloc[2],south_new['Unnamed: 3'].iloc[2],north_east_new['Unnamed: 3'].iloc[2]]}
df_final = pd.DataFrame(data)
print(df_final)                                                                                            
                                                                                            
df_final.to_csv('region-india-a.csv')                                                                                            
