import pandas as pd # type: ignore
import numpy as np # type: ignore

data={
    "Deptartment":['IT','HR','IT','HR','SALES','IT'],
    "Salary":[5000,4000,4500,6000,7500,8000],
    "Age":[25,30,28,32,40,1000],
}
df=pd.DataFrame(data)
Q1 = df['Age'].quantile(0.25)
Q2 = df['Age'].quantile(0.5)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(lower)
print(upper)
Outliers = df[(df['Age'] < lower) | (df['Age'] > upper)]
print(Outliers)
print(IQR)
clean = df[(df['Age'] >= lower) & (df['Age'] <= upper)]
print(clean)