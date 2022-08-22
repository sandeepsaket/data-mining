# -*- coding: utf-8 -*-
"""Data_mining_Assignment_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffjPW1xkuihJhX-KmwDswD6OoOK71dzA
"""

import numpy as np
import pandas as pd
f = []
f1 = pd.read_csv("Andaman nikobar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['35','Andaman Nikobar Island UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Andra Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['28','Andhra Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Arunachal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric)
f.append(['12','Arunachal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Assam.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['18','Assam',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Bihar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['10','Bihar',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chandigarh UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['4','Chandigarh UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chattishgarh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['22','Chattishgarh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['26','Dadra & Nagar Haveli UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Daman & Diu UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['25','Daman & Diu UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Goa.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['30','Goa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Gujrat.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['24','Gujrat',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Haryana.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['6','Haryana',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Himanchal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['2','Himanchal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jammu & Kashmir.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['1','Jammu & Kashmir',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jharkhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['20','Jharkhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Karnataka.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['29','Karnataka',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Kerala.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['32','Kerala',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Lakhadweep.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['31','Lakhadweep UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Madhaya Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['23','Madhaya Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Maharashtra.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['27','Maharashtra',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Manipur.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['14','Manipur',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Meghalaya.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['17','Meghalaya',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Mizoram.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['15','Mizoram',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("NCT of Delhi.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['7','NCT of Delhi',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Nagaland.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['13','Nagaland',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Odisha.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['21','Odhisa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Paducherry UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['34','Paducherry UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Punjab.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['3','Punjab',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Rajasthan.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['8','Rajasthan',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Sikkim.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['11','Sikkim',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tamil Nadu.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['33','Tamil Nadu',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tripura.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['16','Tripura',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttar Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['9','Uttar Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttarakhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['5','Uttarakhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("West Bengal.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['19','West Bengal',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


df = pd.DataFrame(f, columns = ['State Code','States/UT', 'percent-one','percent-two','percent-three'])
df['percent-one'] = df['percent-one'].div(1210193422)
df['percent-two'] = df['percent-two'].div(1210193422)
df['percent-three'] = df['percent-three'].div(1210193422)


p1=((df['percent-one'].sum()))*100    #Total population of India according to census data is 1210193422

p2=((df['percent-two'].sum()))*100

p3 = ((df['percent-three'].sum()))*100



df2 = [['Only One Language Speaker',p1],['Exactly Two Language Speaker',p2],['Three Language or More Speaker',p3]]
dff = pd.DataFrame(df2,columns=['Parts of Question','Percentage'])
print(dff)
print("\n")
print(df)
dff.to_csv('percent-india-1.csv')
df.to_csv('percent-india-2.csv')
"""**Changing dataframe to csv format**"""


