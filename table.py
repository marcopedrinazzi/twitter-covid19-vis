import pandas as pd
import json
import plotly.graph_objects as go
import plotly.offline as pyo
import csv

import dash

# dash dropdown for categories
# dash href for link in cells

data = []
with open('fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index= 0

#with open('table.csv', 'w', newline='', encoding="utf-8") as file:
#        writer = csv.writer(file)
#        writer.writerow(["Tweet", "Link"])
#        for element in data:
#            writer.writerow([data[index]['full_text'],"http://twitter.com/anyuser/status/"+data[index]['id_str']])
#            index= index+1

#print('FINITO')

txt = []
id = []
for element in data:
    txt.append(data[index]['full_text'])
    id.append("http://twitter.com/anyuser/status/"+data[index]['id_str'])
    index=index+1

df = pd.DataFrame(
    {'Tweet': txt,
     'Link': id
    })

print(df)
#df = pd.read_csv('table.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Tweet, df.Link],
               fill_color='lavender',
               align='left'))
])

#fig.show()

pyo.iplot(fig)
