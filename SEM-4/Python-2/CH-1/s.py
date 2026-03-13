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