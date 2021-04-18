#URL count
import pandas as pd
import numpy as np
import json
import sys
import string
import re
# This will load the fields list
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import nltk
from PIL import Image
from collections import Counter
import requests
from bs4 import BeautifulSoup
import datetime
from dateutil.parser import parse
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash

df = pd.read_csv('urls_g.csv',sep=',')
print(df)

app = dash.Dash(__name__)
#https://dash.plotly.com/datatable/filtering
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[{'name': 'Type', 'id':'Type'},
            {'name': 'Link', 'id':'Link', 'type': 'text', 'presentation':'markdown'},
            {'name': 'First-Shared', 'id': 'First-Shared'}],
        data=df.to_dict('records'),
        style_data_conditional=[{
            'if': {
                'column_id': 'Type',
            },
            'font-weight':'bold',
            'width':'200px'
        }],
        style_filter={
            "backgroundColor":"white"
        },
        style_cell={
            'textAlign':'left',
            'font-family': 'Helvetica Neue',
            'border':'0px solid darkslategray',
            'font-size':'16px',
        },
        style_header={
            'backgroundColor':"moccasin", #moccasin
            'font-family':'Helvetica Neue',
            'font-weight': 'bold',
            'border-bottom':'1px solid darkslategray',
            'font-size':'18px',
        },
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current= 0,
        page_size= 12,
    ),
    html.Div(id='datatable-interactivity-container')
])



if __name__ == '__main__':
    app.run_server(debug=True)

