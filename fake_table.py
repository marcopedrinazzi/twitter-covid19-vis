import itertools
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.offline as pyo
from dateutil.parser import parse
from collections import Counter
import csv
import dash
import nltk

csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
        
index= 0

category = []
date = []
txt = []
id = []
cmt_list = []

for element in data:
    token_id = data[index]['id_str']                          
    indice_csv = lista_unica_csv.index(token_id)                
    final_token = token_id + " " +lista_unica_csv[indice_csv+1].lower().replace(" ", "")
    cmt_list.append(final_token)
    
    token=data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y/%m/%d')
    date.append(d)
    
    txt.append(data[index]['full_text'])
    id.append("http://twitter.com/anyuser/status/"+data[index]['id_str'])
    
    index=index+1
    
    
fdist = dict(nltk.FreqDist(cmt_list))
df = pd.DataFrame.from_dict(fdist, orient='index').reset_index()
df = df.rename(columns={'index':'id_str', 0:'count'})
col_one_list = df['id_str'].tolist()
col_two_list = df['count'].tolist()

typelist=[]
namelist=[]

index = 0

count_false = [0] * len(col_one_list)
count_part = [0] * len(col_one_list)

for el in col_one_list:
    tok = el.split()
    namelist.append(tok[0])
    if tok[0] in namelist:
        indx = namelist.index(tok[0])
        if tok[1] == "false":
            count_false[indx] = col_two_list[index]
            category.append(tok[1])
        elif tok[1] == "partiallyfalse":
            count_part[indx] = col_two_list[index]
            category.append(tok[1])
        else:
            print("errore count")
   
    index = index + 1

i=0
for el in col_two_list:
    col_two_list[i] = count_false[i] + count_part[i]
    i = i + 1

df['id_str']=namelist
df['Count False Tweets']=count_false
df['Count Partially False Tweets']=count_part
df['count'] = col_two_list

df = df.sort_values(by=['count'],ascending=[False])

df = pd.DataFrame(
    {'Category': category,
    'Date': date,
    'Tweet': txt,
     'Link': id
    })

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[df.Category,df.Date,df.Tweet, df.Link],
               fill_color='lavender',
               align='left'))
])


pyo.iplot(fig)
