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
print(df)