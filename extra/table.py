import pandas as pd
import json
from dateutil.parser import parse
import plotly.graph_objects as go
import plotly.offline as pyo
import csv

import dash

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index= 0

txt = []
id = []
date = []

for element in data:
    token=data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y/%m/%d')
    date.append(d)
    
    txt.append(data[index]['full_text'])
    id.append("http://twitter.com/anyuser/status/"+data[index]['id_str'])
    
    index=index+1
    

df = pd.DataFrame(
    {'Date': date,
    'Tweet': txt,
     'Link': id
    })

print(df)

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[df.Date,df.Tweet, df.Link],
               fill_color='lavender',
               align='left'))
])


pyo.iplot(fig)
