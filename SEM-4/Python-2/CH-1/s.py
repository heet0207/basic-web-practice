# The code you provided demonstrates different ways to create a DataFrame in Python using the Pandas library. Here's a breakdown of each section:

# DataFrame creation using dictionary
import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
    'Name':['John', 'Alice', 'Bob', 'Charlie'],
    'Age':[25, 30, 22, 28],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data)
print(df)
print()

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
    'Name':['John', 'Alice', 'Bob', 'Charlie'],
    'Age':[25, 30, 22, 28],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data,index=['A', 'B', 'C', 'D'])
print(df)
print()

# DataFrame creation using list of lists

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = [
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 22, 'Chicago'],
]
df=pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
print()

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = [
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 22, 'Chicago'],
]
df=pd.DataFrame(data, columns=['Name', 'Age', 'City'],index=['A', 'B', 'C'])
print(df)
print()

# Dataframe creation using list of dictionaries

import pandas as pd # type: ignore
import numpy as np # type: ignore
data = [
    {'Name':'John', 'Age':25, 'City':'New York'},
    {'Name':'Alice', 'Age':30, 'City':'Los Angeles'},
    {'Name':'Bob', 'Age':22, 'City':'Chicago'},
]
df=pd.DataFrame(data)
print(df)
print()

# DataFrame Creation Using Dictionary of Series

import pandas as pd # type: ignore
import numpy as np # type: ignore

Name= pd.Series(['John', 'Alice', 'Bob'])
Age= pd.Series([25, 30, 22])
data = {
    'Name': Name,
    'Age': Age,
}
df=pd.DataFrame(data)
print(df)
print()


# DataFrame Creation Using NP Array

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = np.array([
    ['John', 25],
    ['Alice', 30],
    ['Bob', 22],
])
df=pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print()


# Task : Dataframe Creation Using Dictoinary of List

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
        'Name':['Pranav','Meet','Rutu','Neelkanth','Riya','Kalpesh'],
        'Age':[17,18,17,18,17,18],
        'City':['Ahmdabad','Surat','Rajkot','Anand','Anand','Jamnagar'],
        'Salary':[1000,2000,3000,4000,5000,6000]
    }

df=pd.DataFrame(data)
print(df)
print()

import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
        'Name':['Pranav','Meet','Rutu','Neelkanth','Riya','Kalpesh'],
        'Age':[17,18,17,18,17,18],
        'City':['Ahmdabad','Surat','Rajkot','Anand','Anand','Jamnagar'],
        'Salary':[1000,2000,3000,4000,5000,6000]
    }

df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
print(df)


# Attribute Of DataFrame


print(df.shape)
print(df.size)
print(df.ndim)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.values)
print(df.info())
print(df.head())
print(df.tail())
print(df.describe())
print(df.sample(3))

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





import pandas as pd # type: ignore
import numpy as np # type: ignore
data = {
        'A':[1,2,4,7],
        'B':[8,9,np.nan,10],
        'C':[np.nan,13,14,15],
        'D':[20,np.nan,33,45]
}
df=pd.DataFrame(data)
df.set_index('A',drop=True,inplace=True)
df.reset_index(inplace=True)
# df.set_index('B',drop=True,inplace=True)
df['E']=['Surat','Kheda','Rajkot','Ahmdabad']
df.loc[4]=[12,32,25,25,'Ahmdabad']
print(df)


import pandas as pd # type: ignore
import numpy as np # type: ignore

df=pd.read_csv('titanic.csv')
df['age']=df['age'].fillna(int(df['age'].mean()))
print(df['age'])
# print(df['age'].fillna(0))
# print(df.isna().sum())
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
# print(df.isnull())
# print(df.isnull().sum())


import pandas as pd # type: ignore
import numpy as np # type: ignore

df=pd.read_csv('titanic.csv')

df['embarked']=df['embarked'].fillna((df['embarked'].mode()[0]))
df['cabin']=df['cabin'].fillna((df['cabin'].mode()[0]))
df['fare']=df['fare'].fillna((df['fare'].mode()[0]))
df['age']=df['age'].fillna(int(df['age'].mean()[0]))
print(df.isnull().sum())



import pandas as pd # type: ignore
import numpy as np # type: ignore

data={
    'Name' : ['A','B','C','D'],
    'City' : ['Ahmadabad','Surat','Rajkot',np.nan],
    'Age' : [20,21,np.nan,np.nan]
}
df=pd.DataFrame(data)
df.dropna(subset=['Name','City'])
print(df.drop_duplicates(keep='first'))
print()
print(df.drop_duplicates(keep='last'))
print()
print(df.drop_duplicates(keep=False))
print(df.duplicated())
# print(df.dropna())
# print()
# print(df.dropna(axis=0)) # 0 => Rows
# print()
# print(df.dropna(axis=1)) # 1 => Columns
df.sum(axis=1, numeric_only=True)

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