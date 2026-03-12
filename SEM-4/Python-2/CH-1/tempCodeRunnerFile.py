import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
    'Name':['John', 'Alice', 'Bob', 'Charlie'],
    'Age':[25, 30, 22, 28],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data,index=['A', 'B', 'C', 'D'])
print(df)