import pandas as pd # type: ignore
import numpy as np # type: ignore

data = {
    'Gender':['Male', 'Female', 'Male','Female','Male'],
    'Result':['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
}
df=pd.DataFrame(data)
print(df)
print(pd.crosstab(df['Gender'],df['Result'],margins=True))