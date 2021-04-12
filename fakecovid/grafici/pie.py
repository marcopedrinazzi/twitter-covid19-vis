import plotly.express as px
import json
import pandas as pd
import csv
import itertools
from collections import Counter

csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))


category = []
index = 0

for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    category.append(lista_unica_csv[indice_csv+1].lower())
    index=index+1

count = Counter(category)

df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'category', 0:'count'})

colors = ['gold', 'mediumturquoise']

fig = px.pie(df, values='count', names='category',
             title='Tweets percentage classified by category')
fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=0.8)))
fig.show()