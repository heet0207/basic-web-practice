import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('titanic.csv') # type: ignore
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True,cbar=True)
plt.show()

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('titanic.csv') # type: ignore
sns.scatterplot(x='age',y='fare',data=df, hue='survived')
plt.show()

import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('titanic.csv') # type: ignore
sns.boxplot(x='pclass',y='fare',data=df, hue='survived')
plt.show()