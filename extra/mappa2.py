import pandas as pandas
import plotly.express as px

df = pandas.read_csv('mappa.csv')
lista =df['Count'].to_list()

fig = px.scatter_geo(df, lat='Lat',lon='Long', color='Continent',
                     hover_name="Text", size="Count",
                     animation_frame="Dates",animation_group='T',
                     projection="natural earth")


fig.show()