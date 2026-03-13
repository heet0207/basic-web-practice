import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
        'Name':['Pranav', np.nan,'Rutu','Neelkanth','Riya','Kalpesh'],
        'Age':[17,np.nan,17,18,17,18],
        'City':['Ahmdabad',np.nan,'Rajkot','Anand','Anand','Jamnagar'],
        'Salary':[1000,2000,3000,4000,5000,np.nan]
    }
df=pd.DataFrame(data)
print(df.loc[1])
print(df.iloc[1])
print(df.loc[2,'Salary'])
print(df.iloc[2,1])