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

csv_dataframe = pd.read_csv('dataset/fakecovid_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('dataset/fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
cmt_list = []
stopwords = set(STOPWORDS) 
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['user']['screen_name']
    #token_ver = data[index]['user']['verified']
    final_token = token + " " +lista_unica_csv[indice_csv+1].lower().replace(" ", "")
    cmt_list.append(final_token)
    index=index+1
    


fdist = dict(nltk.FreqDist(cmt_list))
df = pd.DataFrame.from_dict(fdist, orient='index').reset_index()
df = df.rename(columns={'index':'usernames', 0:'count'})
col_one_list = df['usernames'].tolist()
col_two_list = df['count'].tolist()

typelist=[]
namelist=[]

index = 0

count_false = [0] * len(col_one_list)
count_part = [0] * len(col_one_list)
count_true = [0] * len(col_one_list)
count_other = [0] * len(col_one_list)
count_unproven = [0] * len(col_one_list)
print("count false len "+str(len(count_false)))

for el in col_one_list:
    tok = el.split()
    namelist.append(tok[0])
    #typelist.append(tok[1])
    if tok[0] in namelist:
        indx = namelist.index(tok[0])
        if tok[1] == "false":
            count_false[indx] = col_two_list[index]
        elif tok[1] == "partiallyfalse":
            count_part[indx] = col_two_list[index]
        elif tok[1] == "unproven":
            count_unproven[indx] = col_two_list[index]
        elif tok[1] == "others":
            count_other[indx] = col_two_list[index]
        elif tok[1] == "true":
            count_true[indx] = col_two_list[index]
        else:
            print("errore count")
   
    index = index + 1

i=0
for el in col_two_list:
    col_two_list[i] = count_false[i] + count_part[i] + count_unproven[i] + count_other[i] + count_true[i]
    i = i + 1

print("count false len "+str(len(count_false)))
df['usernames']=namelist
df['Count False Tweets']=count_false
df['Count Partially False Tweets']=count_part
df['Count Unproven Tweets']=count_unproven
df['Counter Other Tweets']=count_other
df['Counter True Tweets']=count_true
df['count'] = col_two_list
#del df['count']

#print(df.to_string())
#df['type']=typelist

df = df.sort_values(by=['count'],ascending=[False])

print(df.head(21).to_string())

#versione vertical
#chart = alt.Chart(df).transform_fold(
#    ['Count False Tweets', 'Count Partially False Tweets', 'Count Unproven Tweets', 'Counter Other Tweets', 'Counter True Tweets'],
#).mark_bar().encode( 
#   x='usernames:N',
#    y='value:Q', 
#    color='key:N'
#).transform_filter(
#    alt.FieldRangePredicate(field='count', range=[5, 35])
#)


bars = alt.Chart(df).transform_fold(
    ['Count False Tweets', 'Count Partially False Tweets', 'Count Unproven Tweets', 'Counter Other Tweets', 'Counter True Tweets'],
).mark_bar().encode(
    x=alt.X('value:Q'),
    y=alt.Y('usernames:N'),
    color=alt.Color('key:N')
).transform_filter(
    alt.FieldRangePredicate(field='count', range=[5, 35])
)

bars.show()


