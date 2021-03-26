import json
from collections import Counter
import pandas as pd
import altair as alt
import datetime
from dateutil.parser import parse

data = []
with open('../dataset/fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))


lista = []
index = 0

for element in data: 
    token=data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y/%m/%d')
    lista.append(d)
    index=index+1


count=Counter(lista)
df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'data', 0:'tweet_count'})

print(df)

chart = alt.Chart(
    df,
    title="Tweet count hetmap"
).mark_rect().encode(
    x='date(data):O',
    y='month(data):O',
    color=alt.Color('tweet_count:Q', scale=alt.Scale(scheme="inferno")),
    tooltip=[
        alt.Tooltip('monthdate(data):T', title='Date'),
        alt.Tooltip('tweet_count:Q', title='Tweet Count')
    ]
).properties(width=550)

chart.show()
