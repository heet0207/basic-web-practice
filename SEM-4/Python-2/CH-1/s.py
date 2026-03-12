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