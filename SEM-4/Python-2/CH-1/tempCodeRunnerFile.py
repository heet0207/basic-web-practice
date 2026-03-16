import pandas as pd # type: ignore
import numpy as np # type: ignore

data={
    'Name' : ['A','B','A','D'],
    'City' : ['Ahmadabad','Surat','Ahmadabad','Rajkot'],
    'Age' : [20,21,20,30]
    }
df=pd.DataFrame(data)
print(df)
print(df.drop_duplicates(keep='first'))
print(df.drop_duplicates(keep='last'))
print(df.drop_duplicates(keep=False))
print(df.duplicated())