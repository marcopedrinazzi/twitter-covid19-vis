import pandas as pd
import numpy as np
import json
import sys
import string
import re
import itertools  
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import nltk
from PIL import Image
import altair as alt
import csv
pd.options.mode.chained_assignment = None

csv_dataframe = pd.read_csv('fakecovid_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
print(csv_dataframe)

data = []
with open('fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

#filtro gli ID in quanto il dataset contiene dei tweet non piu disponibili (circa 100)
index_id = 0
id_list = []
for element in data:
    id_list.append(data[index_id]['id_str'])
    index_id=index_id+1

boolean_series = csv_dataframe.tweet_id.isin(id_list)
filtered_df = csv_dataframe[boolean_series]
filtered_df.to_csv('fakecovid_filtered_dataset_clean.csv',sep=';',index=False)

