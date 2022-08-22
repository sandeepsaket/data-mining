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



import numpy as np
import pandas as pd
f = []
f1 = pd.read_csv("Andaman nikobar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Andaman Nikobar Island UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Andra Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Andhra Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Arunachal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric)
f.append(['Arunachal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Assam.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Assam',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Bihar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Bihar',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chandigarh UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Chandigarh UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chattishgarh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Chattishgarh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Dadra & Nagar Haveli UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Daman & Diu UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Daman & Diu UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Goa.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Goa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Gujrat.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Gujrat',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Haryana.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Haryana',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Himanchal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Himanchal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jammu & Kashmir.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Jammu & Kashmir',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jharkhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Jharkhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Karnataka.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Karnataka',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Kerala.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Kerala',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Lakhadweep.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Lakhadweep UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Madhaya Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Madhaya Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Maharashtra.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Maharashtra',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Manipur.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Manipur',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Meghalaya.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Meghalaya',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Mizoram.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Mizoram',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("NCT of Delhi.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['NCT of Delhi',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Nagaland.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Nagaland',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Odisha.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Odhisa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Paducherry UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Paducherry UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Punjab.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Punjab',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Rajasthan.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Rajasthan',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Sikkim.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Sikkim',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tamil Nadu.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Tamil Nadu',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tripura.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Tripura',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttar Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Uttar Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttarakhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Uttarakhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("West Bengal.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['West Bengal',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


df = pd.DataFrame(f, columns = ['States/UT', 'Only One Language Speaker','Exactly Two Language Speaker','Three Language or More Speaker'])

p1=((df['Only One Language Speaker'].sum()) / 1210193422)*100    #Total population of India according to census data is 1210193422

p2=((df['Exactly Two Language Speaker'].sum()) / 1210193422)*100

p3 = ((df['Three Language or More Speaker'].sum()) / 1210193422)*100



df2 = [['Only One Language Speaker',p1],['Exactly Two Language Speaker',p2],['Three Language or More Speaker',p3]]
dff = pd.DataFrame(df2,columns=['Parts of Question','Percentage'])





lis=[]

for k in range(0,35):
    lis.append((df['Three Language or More Speaker'][k])/(df['Exactly Two Language Speaker'][k]))
    
s = pd.Series(lis, index=df.index)

df['3-2 Percent'] = s.values

df4=df.sort_values('3-2 Percent')

df5 = df4['States/UT']

df6 = [['1st Top most',df5.iloc[34]],['2nd top most',df5.iloc[33]],['3rd top most',df5.iloc[32]],['1st most worst three',df5.iloc[0]],['2nd most worst three',df5.iloc[1]],['3rd most worst three',df5.iloc[2]]]

dff = pd.DataFrame(df6,columns=['Parts of question','States'])


print(dff)
dff.to_csv('3-to-2-ratio.csv')




       



import numpy as np
import pandas as pd
f = []
f1 = pd.read_csv("Andaman nikobar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Andaman Nikobar Island UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Andra Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Andhra Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Arunachal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric)
f.append(['Arunachal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd
f1 = pd.read_csv("Assam.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 
f.append(['Assam',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Bihar.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Bihar',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chandigarh UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Chandigarh UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Chattishgarh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Chattishgarh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Dadra & Nagar haveli UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Dadra & Nagar Haveli UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Daman & Diu UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Daman & Diu UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Goa.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Goa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Gujrat.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Gujrat',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Haryana.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Haryana',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Himanchal Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Himanchal Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jammu & Kashmir.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Jammu & Kashmir',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Jharkhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Jharkhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Karnataka.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Karnataka',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Kerala.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Kerala',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Lakhadweep.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Lakhadweep UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Madhaya Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Madhaya Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Maharashtra.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Maharashtra',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Manipur.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Manipur',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Meghalaya.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Meghalaya',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Mizoram.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Mizoram',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("NCT of Delhi.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['NCT of Delhi',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Nagaland.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Nagaland',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Odisha.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Odhisa',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Paducherry UT.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Paducherry UT',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Punjab.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Punjab',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Rajasthan.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Rajasthan',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Sikkim.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Sikkim',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tamil Nadu.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Tamil Nadu',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Tripura.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Tripura',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttar Pradesh.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Uttar Pradesh',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("Uttarakhand.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['Uttarakhand',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


import numpy as np
import pandas as pd

f1 = pd.read_csv("West Bengal.csv")
f2 = f1[['Unnamed: 4','Unnamed: 9','Unnamed: 14']].iloc[4:].fillna(0)
f2 = f2.apply(pd.to_numeric) 

f.append(['West Bengal',f2['Unnamed: 4'].sum() - f2['Unnamed: 9'].sum(),f2['Unnamed: 9'].sum() - f2['Unnamed: 14'].sum(),f2['Unnamed: 14'].sum()])


df = pd.DataFrame(f, columns = ['States/UT', 'Only One Language Speaker','Exactly Two Language Speaker','Three Language or More Speaker'])

p1=((df['Only One Language Speaker'].sum()) / 1210193422)*100    #Total population of India according to census data is 1210193422

p2=((df['Exactly Two Language Speaker'].sum()) / 1210193422)*100

p3 = ((df['Three Language or More Speaker'].sum()) / 1210193422)*100



df2 = [['Only One Language Speaker',p1],['Exactly Two Language Speaker',p2],['Three Language or More Speaker',p3]]
dff = pd.DataFrame(df2,columns=['Parts of Question','Percentage'])


lis1=[]
for k in range(0,35):
    
    lis1.append((df['Exactly Two Language Speaker'][k])/(df['Only One Language Speaker'][k]))

s1 = pd.Series(lis1, index=df.index)

df['2-1 Percent'] = s1.values

df7=df.sort_values('2-1 Percent')

df8=df7['States/UT']

df9 = [['1st Top most',df8.iloc[34]],['2nd top most',df8.iloc[33]],['3rd top most',df8.iloc[32]],['1st most worst three',df8.iloc[0]],['2nd most worst three',df8.iloc[1]],['3rd most worst three',df8.iloc[2]]]

dff_1 = pd.DataFrame(df9,columns=['Parts of question','States'])


print(dff_1)
dff.to_csv('2-to-1-ratio.csv')



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






import pandas as pd
import numpy as np

df = pd.read_csv('Education level and sex.csv')

df = df[['Unnamed: 2','Unnamed: 4','Unnamed: 8']]


df['Unnamed: 8'].iloc[5:] = df['Unnamed: 8'].iloc[5:].apply(pd.to_numeric)


df1 = pd.DataFrame()


for i in range (0,864,24):
    df1 = (df1.append(df.iloc[8+i:13+i]))

df1['Unnamed: 8'] = df1['Unnamed: 8'].apply(pd.to_numeric)
df1.index = pd.RangeIndex(len(df1.index))

f = []
count = 0
for i in range(5,869,24):
    k = count
    for j in range(k,k+5):
        f.append(((df1['Unnamed: 8'].iloc[j])/(df['Unnamed: 8'].iloc[i]))*100)
        count = count+1

df2 = pd.DataFrame(f,columns = ['percentage'])



c_df = pd.concat([df1[['Unnamed: 2','Unnamed: 4']],df2],axis=1)
c_df = c_df.rename(columns={'Unnamed: 2':'States/UT','Unnamed: 4':'literacy-group','percentage':'percentage'})


n = 0
max_index = []
for x in range(0,36):
    c = n
    max_index.append(c_df['percentage'].iloc[c:c+5].idxmax())
    n = n+5

fdx = pd.DataFrame()
for a in range(0,len(max_index)):
    fdx = fdx.append(c_df.iloc[max_index[a]])
fdx.index = pd.RangeIndex(len(fdx.index))

print(fdx)

fdx.to_csv('literacy-india.csv')







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






import pandas as pd
import numpy as np

df = pd.read_csv('Education level and sex.csv')

df1 = pd.DataFrame()
df = (df[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2','Unnamed: 4','Unnamed: 6','Unnamed: 9','Unnamed: 10']][5:])
df[['Unnamed: 9','Unnamed: 10']] =  df[['Unnamed: 9','Unnamed: 10']].apply(pd.to_numeric)

for i in range(1,865,24):
    df1 = (df1.append(df.iloc[i:7+i]))
df1.index = pd.RangeIndex(len(df1.index))

m = []
f = []
count = 0
for i in range(0,864,24):
    k = count
    for j in range(k,k+7):
        m.append(((df1['Unnamed: 9'].iloc[j])/(df['Unnamed: 9'].iloc[i])))
        f.append(((df1['Unnamed: 10'].iloc[j])/(df['Unnamed: 10'].iloc[i])))
        count = count+1
     
df2 = pd.DataFrame(m,columns = ['male-ratio'])
df3 = pd.DataFrame(f,columns = ['female-ratio'])


c_df = pd.concat([df1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2','Unnamed: 4']],df2,df3],axis=1)

n = 0
max_index_1 = []
max_index_2 = []
for x in range(0,36):
    c = n
    max_index_1.append(c_df['male-ratio'].iloc[c:c+7].idxmax())
    max_index_2.append(c_df['female-ratio'].iloc[c:c+7].idxmax())
    n = n+7

fdx_1 = pd.DataFrame()
fdx_2 = pd.DataFrame()
for a in range(0,len(max_index_1)):
    fdx_1 = fdx_1.append(c_df.iloc[max_index_1[a]])
    fdx_2 = fdx_2.append(c_df.iloc[max_index_2[a]])
fdx_1.index = pd.RangeIndex(len(fdx_1.index))
fdx_1 = fdx_1.rename(columns={'Unnamed: 4': 'literacy-group-males'})
fdx_2.index = pd.RangeIndex(len(fdx_2.index))
fdx_2 = fdx_2.rename(columns={'Unnamed: 4': 'literacy-group-females'})

c_df_1 = pd.concat([fdx_1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2']],fdx_1[['literacy-group-males','male-ratio']],fdx_2[['literacy-group-females','female-ratio']]],axis=1)
c_df_1 = c_df_1.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'States/UT Code','Unnamed: 2':'States/UT'})
print(" highest ratio of population that can speak 3 or more languages")
print(c_df_1)
c_df_1.to_csv('literacy-gender-1.csv')
del df1,df2,df3,c_df,fdx_1,fdx_2,c_df_1
max_index_1.clear()
max_index_2.clear()

## part 2
df = pd.read_csv('Education level and sex.csv')
df1 = pd.DataFrame()
df = (df[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2','Unnamed: 4','Unnamed: 6','Unnamed: 7']][5:])
df[['Unnamed: 6','Unnamed: 7']] =  df[['Unnamed: 6','Unnamed: 7']].apply(pd.to_numeric)

for i in range(1,865,24):
    df1 = (df1.append(df.iloc[i:7+i]))
df1.index = pd.RangeIndex(len(df1.index))

m = []
f = []
count = 0
for i in range(0,864,24):
    k = count
    for j in range(k,k+7):
        m.append(((df1['Unnamed: 6'].iloc[j])/(df['Unnamed: 6'].iloc[i])))
        f.append(((df1['Unnamed: 7'].iloc[j])/(df['Unnamed: 7'].iloc[i])))
        count = count+1
     
df2 = pd.DataFrame(m,columns = ['male-ratio'])
df3 = pd.DataFrame(f,columns = ['female-ratio'])

c_df = pd.concat([df1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2','Unnamed: 4']],df2,df3],axis=1)

n = 0
max_index_1 = []
max_index_2 = []
for x in range(0,36):
    c = n
    max_index_1.append(c_df['male-ratio'].iloc[c:c+7].idxmax())
    max_index_2.append(c_df['female-ratio'].iloc[c:c+7].idxmax())
    n = n+7

fdx_1 = pd.DataFrame()
fdx_2 = pd.DataFrame()
for a in range(0,len(max_index_1)):
    fdx_1 = fdx_1.append(c_df.iloc[max_index_1[a]])
    fdx_2 = fdx_2.append(c_df.iloc[max_index_2[a]])
fdx_1.index = pd.RangeIndex(len(fdx_1.index))
fdx_1 = fdx_1.rename(columns={'Unnamed: 4': 'literacy-group-males'})
fdx_2.index = pd.RangeIndex(len(fdx_2.index))
fdx_2 = fdx_2.rename(columns={'Unnamed: 4': 'literacy-group-females'})

c_df_1 = pd.concat([fdx_1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX','Unnamed: 2']],fdx_1[['literacy-group-males','male-ratio']],fdx_2[['literacy-group-females','female-ratio']]],axis=1)
c_df_1 = c_df_1.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'States/UT Code','Unnamed: 2':'States/UT'})
print(" highest ratio of population that can speak exactly 2 language ")
print(c_df_1)
c_df_1.to_csv('literacy-gender-2.csv')
