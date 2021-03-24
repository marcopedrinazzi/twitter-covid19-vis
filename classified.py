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
import itertools

csv_dataframe = pd.read_csv('fakecovid_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
cmt_list = []
stopwords = set(STOPWORDS) 
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['user']['screen_name']
    final_token = token + " " +lista_unica_csv[indice_csv+1].lower().replace(" ", "")
    cmt_list.append(final_token)
    index=index+1
    


fdist = dict(nltk.FreqDist(cmt_list))
df = pd.DataFrame.from_dict(fdist, orient='index').reset_index()
df = df.rename(columns={'index':'usernames', 0:'count'})
col_one_list = df['usernames'].tolist()

typelist=[]
namelist=[]
index = 0
for el in col_one_list:
    #elm = re.findall("partiallyfalse|false|unproven|true|others", el)
    #print(el + str(elm) +str(index))
    #typelist.append(elm)
    tok = el.split()
    namelist.append(tok[0])
    typelist.append(tok[1])

#typelist=list(itertools.chain.from_iterable(typelist))
#df['type']=typelist
#print(df)
df['usernames']=namelist
df['type']=typelist

df = df.sort_values(by=['count'],ascending=False)
print(df.to_string())

cha = alt.Chart(
    df,
).mark_bar().encode(
    x=alt.X('usernames:N'),
    y=alt.Y('count:Q',stack=None),
    color='type'
)
cha.show()
