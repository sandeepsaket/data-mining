import numpy as np
import pandas as pd
f = []
f1 = pd.read_csv("Andaman nikobar.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['35','Andaman Nikobar Island UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Andra Pradesh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['28','Andhra Pradesh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Arunachal Pradesh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric)
f.append(['12','Arunachal Pradesh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Assam.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['18','Assam',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Bihar.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['10','Bihar',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chandigarh UT.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['4','Chandigarh UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chattishgarh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['22','Chattishgarh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['26','Dadra & Nagar Haveli UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Daman & Diu UT.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['25','Daman & Diu UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Goa.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['30','Goa',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Gujrat.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['24','Gujrat',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Haryana.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['6','Haryana',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Himanchal Pradesh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['2','Himanchal Pradesh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jammu & Kashmir.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['1','Jammu & Kashmir',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jharkhand.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['20','Jharkhand',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Karnataka.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['29','Karnataka',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Kerala.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['32','Kerala',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Lakhadweep.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['31','Lakhadweep UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Madhaya Pradesh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['23','Madhaya Pradesh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Maharashtra.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['27','Maharashtra',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Manipur.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['14','Manipur',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Meghalaya.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['17','Meghalaya',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Mizoram.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['15','Mizoram',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("NCT of Delhi.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['7','NCT of Delhi',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Nagaland.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['13','Nagaland',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Odisha.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['21','Odhisa',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Paducherry UT.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['34','Paducherry UT',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Punjab.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['3','Punjab',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Rajasthan.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['8','Rajasthan',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Sikkim.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['11','Sikkim',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tamil Nadu.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['33','Tamil Nadu',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tripura.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['16','Tripura',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttar Pradesh.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['9','Uttar Pradesh',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttarakhand.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['5','Uttarakhand',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("West Bengal.csv")
f2 = f1[['Unnamed: 5','Unnamed: 10','Unnamed: 15']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['19','West Bengal',f2['Unnamed: 5'].sum() - f2['Unnamed: 10'].sum(),f2['Unnamed: 10'].sum() - f2['Unnamed: 15'].sum(),f2['Unnamed: 15'].sum()])


df = pd.DataFrame(f, columns = ['State Code','States/UT', 'male-percent-one','male-percent-two','male-percent-three'])
df['male-percent-one'] = df['male-percent-one'].div(1210193422)
df['male-percent-two'] = df['male-percent-two'].div(1210193422)
df['male-percent-three'] = df['male-percent-three'].div(1210193422)


p1=((df['male-percent-one'].sum()))*100    #Total population of India according to census data is 1210193422

p2=((df['male-percent-two'].sum()))*100

p3 = ((df['male-percent-three'].sum()))*100



df2 = [['Only One Language Speaker',p1],['Exactly Two Language Speaker',p2],['Three Language or More Speaker',p3]]
dff = pd.DataFrame(df2,columns=['Parts of Question','Male-Percentage'])
print(dff)
print("\n")
print(df)
dff.to_csv('male-percent-india-1.csv')
df.to_csv('male-percent-india-2.csv')
"""**Changing dataframe to csv format**"""
df['male-percentage'] = df['male-percent-one']+df['male-percent-two']+df['male-percent-three']

dff1 = pd.DataFrame(df['male-percentage'],columns=['male-percentage'])

del df2,dff,df,p1,p2,p3,f1,f2,f
##Female


import numpy as np
import pandas as pd
f = []
f1 = pd.read_csv("Andaman nikobar.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['35','Andaman Nikobar Island UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Andra Pradesh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['28','Andhra Pradesh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Arunachal Pradesh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric)
f.append(['12','Arunachal Pradesh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Assam.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['18','Assam',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Bihar.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['10','Bihar',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chandigarh UT.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['4','Chandigarh UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chattishgarh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['22','Chattishgarh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['26','Dadra & Nagar Haveli UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Daman & Diu UT.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['25','Daman & Diu UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Goa.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['30','Goa',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Gujrat.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['24','Gujrat',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Haryana.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['6','Haryana',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Himanchal Pradesh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['2','Himanchal Pradesh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jammu & Kashmir.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['1','Jammu & Kashmir',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jharkhand.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['20','Jharkhand',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Karnataka.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['29','Karnataka',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Kerala.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['32','Kerala',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Lakhadweep.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['31','Lakhadweep UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Madhaya Pradesh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['23','Madhaya Pradesh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Maharashtra.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['27','Maharashtra',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Manipur.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['14','Manipur',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Meghalaya.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['17','Meghalaya',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Mizoram.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['15','Mizoram',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("NCT of Delhi.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['7','NCT of Delhi',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Nagaland.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['13','Nagaland',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Odisha.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['21','Odhisa',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Paducherry UT.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['34','Paducherry UT',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Punjab.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['3','Punjab',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Rajasthan.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['8','Rajasthan',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Sikkim.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['11','Sikkim',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tamil Nadu.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['33','Tamil Nadu',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tripura.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['16','Tripura',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttar Pradesh.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['9','Uttar Pradesh',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttarakhand.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['5','Uttarakhand',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("West Bengal.csv")
f2 = f1[['Unnamed: 6','Unnamed: 11','Unnamed: 16']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['19','West Bengal',f2['Unnamed: 6'].sum() - f2['Unnamed: 11'].sum(),f2['Unnamed: 11'].sum() - f2['Unnamed: 16'].sum(),f2['Unnamed: 16'].sum()])


df = pd.DataFrame(f, columns = ['State Code','States/UT', 'female-percent-one','female-percent-two','female-percent-three'])
df['female-percent-one'] = df['female-percent-one'].div(1210193422)
df['female-percent-two'] = df['female-percent-two'].div(1210193422)
df['female-percent-three'] = df['female-percent-three'].div(1210193422)


p1=((df['female-percent-one'].sum())*100)    #Total population of India according to census data is 1210193422

p2=((df['female-percent-two'].sum())*100)

p3 = ((df['female-percent-three'].sum())*100)



df2 = [['Only One Language Speaker',p1],['Exactly Two Language Speaker',p2],['Three Language or More Speaker',p3]]
dff = pd.DataFrame(df2,columns=['Parts of Question','Female-Percentage'])
print(dff)
print("\n")
print(df)
dff.to_csv('female-percent-india-1.csv')
df.to_csv('female-percent-india-2.csv')
"""**Changing dataframe to csv format**"""

df['female-percentage'] = df['female-percent-one']+df['female-percent-two']+df['female-percent-three']
dff2 = pd.DataFrame(df['female-percentage'],columns=['female-percentage'])
concatenated_dataframes = pd.concat([dff1, dff2], axis=1)
print(concatenated_dataframes)
