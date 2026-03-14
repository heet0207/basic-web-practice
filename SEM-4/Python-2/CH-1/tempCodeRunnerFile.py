import pandas as pd # type: ignore
import numpy as np # type: ignore

df=pd.read_csv('titanic.csv')
# print(df)
# print(df.describe(include='int64'))
# print(df.describe(exclude='int64'))
#print(df.describe(include='all'))
#print(df['embarked'].unique())
# print(df['age'].nunique())
# print(df['sex'].unique())
# print(df['embarked'].value_counts()['S'])
# print((df['embarked']=='S').sum())
# print(df['sex'].value_counts()['male'])
# print((df['sex']=='male').sum())
# print(df.nunique())
print(df.isnull())
print(df.isnull().sum())