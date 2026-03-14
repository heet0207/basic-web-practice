import pandas as pd # type: ignore
import numpy as np # type: ignore

df=pd.read_csv('titanic.csv')
# print(df)
# print(df.describe(include='int64'))
# print(df.describe(exclude='int64'))
#print(df.describe(include='all'))
#print(df['embarked'].unique())
#print(df['age'].unique())
print(df['sex'].unique())