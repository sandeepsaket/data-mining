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

