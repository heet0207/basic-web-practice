
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('titanic.csv') # type: ignore
sns.boxplot(x='pclass',y='fare',data=df, hue='survived')
plt.show()