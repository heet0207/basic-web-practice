import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import plotly.io as pio # type: ignore


data = {
    'Name':['A','B','C','D','E','F'],
    'Age':[20,22,24,26,28,30],
    'PClass':[1,2,3,1,2,3],
    'Gender':['Male', 'Female', 'Male','Female','Male','Female'],
    'Fare':[200,300,150,400,500,550]
}
df = pd.DataFrame(data)
# fig = px.bar(df, x='Name', y='Age',color='Fare',barmode='group',title='A Bar Chart',orientation='v')
#fig = px.scatter(df,x='Age',y='Fare',color='Name',size='PClass',facet_row='Gender',facet_col='Gender')
# fig = px.scatter_3d(df,x='PClass',y='Age',z='Fare',color='Gender')
fig = px.pie(df,names='PClass',values='Age')
fig = px.pie(df,names='Name',color_discrete_sequence=['blue','red','green'])
fig.show()