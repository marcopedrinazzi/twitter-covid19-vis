import itertools
import pandas as pd
import json
#import plotly.graph_objects as go
#import plotly.offline as pyo
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
link = []

for element in data:
    token_id = data[index]['id_str']                          
    indice_csv = lista_unica_csv.index(token_id)   
    value_cat =  lista_unica_csv[indice_csv+1].lower()
    if value_cat == "false":
        value_cat = "fake"
    category.append(value_cat.replace(" ", ""))
    
    token=data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y/%m/%d')
    date.append(d)
    
    txt.append(remove_urls(data[index]['full_text']))
    link.append("[http://twitter.com/anyuser/status/"+data[index]['id_str']+"](http://twitter.com/anyuser/status/"+data[index]['id_str']+")")
    index=index+1

df = pd.DataFrame(
    {'Type': category,
    'Date': date,
    'Tweet': txt,
    'Link': link
    })


app = dash.Dash(__name__)
#https://dash.plotly.com/datatable/filtering
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {'name': 'Type', 'id': 'Type'},
            {'name': 'Date', 'id': 'Date'},
            {'name': 'Tweet', 'id': 'Tweet'},
            {'name': 'Link', 'id':'Link', 'type': 'text', 'presentation':'markdown'}],
        data=df.to_dict('records'),
        style_filter={
            "backgroundColor":"white"
        },
        style_data_conditional=[
        {
            'if': {
                'column_id': 'Type',
            },
            'font-weight':'bold'
        }],
        style_cell={
            'textAlign':'left',
            'font-family': 'Calibri',
            'whiteSpace': 'normal',
            'padding': '10px',
            'border':'0.8px solid darkslategray',
            'font-size':'16px',
            'height': 'auto'
        },
        style_header={
            'backgroundColor':"moccasin",
            'font-family':'Calibri',
            'font-weight': 'bold',
            'whiteSpace': 'normal',
            'padding': '10px',
            'border':'0.8px solid darkslategray',
            'font-size':'20px',
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
        page_size= 8,
        fill_width=False
    ),
    html.Div(id='datatable-interactivity-container')
])



if __name__ == '__main__':
    app.run_server(debug=True)

