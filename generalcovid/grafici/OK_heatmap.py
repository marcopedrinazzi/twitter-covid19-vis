import json
from collections import Counter
import pandas as pd
import altair as alt
import datetime
from dateutil.parser import parse


data = []
with open('general_result.json', 'r') as f:
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

start = datetime.datetime.strptime("2020/01/01", "%Y/%m/%d")
end = datetime.datetime.strptime("2020/10/01", "%Y/%m/%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y/%m/%d") not in count:
        print(date.strftime("%Y/%m/%d") )
        count[date.strftime("%Y/%m/%d")] = 0

df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'data', 0:'tweet_count'})

chart = alt.Chart(
    df,
    title="Tweet count hetmap"
).mark_rect().encode(
    x='date(data):O',
    y='month(data):O',
    color=alt.Color('tweet_count:Q', scale=alt.Scale(scheme="bluepurple")),
    tooltip=[
        alt.Tooltip('monthdate(data):T', title='Date'),
        alt.Tooltip('tweet_count:Q', title='Tweet Count')
    ]
).properties(width=550)

chart.show()