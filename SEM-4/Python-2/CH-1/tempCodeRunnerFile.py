
import pandas as pd # type: ignore
import numpy as np # type: ignore

df=pd.read_csv('titanic.csv')
df['age']=df['age'].fillna(int(df['age'].mean()))
print(df['age'])