#import itertools
import pandas as pd
import json
#import plotly.graph_objects as go
#import plotly.offline as pyo
from dateutil.parser import parse
#from collections import Counter
#import csv
import dash
import nltk
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import re

# external CSS stylesheets
external_stylesheets = ['assets/style.css']

def remove_urls(text):
    result = re.sub(r"http\S+", "", text)
    return(result)

data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
        
index= 0

category = []
date = []
txt = []
id = []
cmt_list = []

for element in data:
    token=data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y/%m/%d')
    date.append(d)
    
    txt.append(remove_urls(data[index]['full_text']))
    id.append("http://twitter.com/anyuser/status/"+data[index]['id_str'])
    
    index=index+1
    

df = pd.DataFrame(
    {'Date': date,
    'Tweet': txt,
     'Link': id
    })

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
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
            'font-family': 'Calibri',
            'whiteSpace': 'normal',
            'padding': '16px',
            'border':'0.5px solid darkslategray',
            'font-size':'15px',
            'height': 'auto'
        },
        style_header={
            'backgroundColor':"moccasin",
            'font-family':'Calibri',
            'font-weight': 'bold',
            'whiteSpace': 'normal',
            'padding': '16px',
            'border':'0.5px solid darkslategray',
            'font-size':'19px',
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

# In style.css sfruttare gli id indicati.
#https://dash.plotly.com/external-resources
#https://dash.plotly.com/layout
#https://community.plotly.com/t/dash-datatable-style-filter-doesnt-seem-to-work/15691


if __name__ == '__main__':
    app.run_server(debug=False)

