import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore

df = pd.read_csv('titanic.csv') # type: ignore
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True,cmap='coolwarm',cbar=True)
plt.show()