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
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import re

def remove_urls(text):
    result = re.sub(r"http\S+", "", text)
    return(result)


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
    
    txt.append(remove_urls(data[index]['full_text']))
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
        if tok[1] == "false":
            category.append("fake")
        elif tok[1] == "partiallyfalse":
            category.append(tok[1])
        else:
            print("errore count")
   
    index = index + 1


df = pd.DataFrame(
    {'Category': category,
    'Date': date,
    'Tweet': txt,
     'Link': id
    })

app = dash.Dash(__name__)
#https://dash.plotly.com/datatable/filtering
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i} for i in df.columns
        ],
        data=df.to_dict('records'),
        style_filter={
            "backgroundColor":"white"
        },
        style_cell={
            'textAlign':'left',
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_header={
            'backgroundColor':"paleturquoise",
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        },
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current= 0,
        page_size= 10,
        fill_width=False
    ),
    html.Div(id='datatable-interactivity-container')
])



if __name__ == '__main__':
    app.run_server(debug=True)

