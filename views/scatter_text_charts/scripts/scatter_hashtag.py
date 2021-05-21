import json
import pandas as pd
import csv
import itertools
import demoji
from collections import Counter
import nltk
import altair as alt

alt.data_transformers.disable_max_rows()

data = []
with open('twitter-covid19-vis/fakecovid/dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

data1 = []
with open('general_result_translated_full.json', 'r') as f1:
    for line in f1:
        data1.append(json.loads(line))

index=0
hasht = []
for element in data:
    for entity in data[index]['entities']['hashtags']:
        entity['text'] = entity['text'].lower().replace(" ", "")
        hasht.append(entity['text'] + " " + "generalcovid")
    index=index+1

index1= 0
hasht1 = []
for element in data1:
    for entity in data1[index1]['entities']['hashtags']:
        entity['text'] = entity['text'].lower().replace(" ", "")
        hasht1.append(entity['text'] + " " + "fakecovid")
    index1=index1+1

merged_final = hasht + hasht1

c = dict(nltk.FreqDist(merged_final))

df = pd.DataFrame.from_dict(c, orient='index').reset_index()
df = df.rename(columns={'index':'Hashtag', 0:'Count'})

col_one_list = df['Hashtag'].tolist()
col_two_list = df['Count'].tolist()

count_general= [0] * len(col_one_list)
count_fake = [0] * len(col_one_list)

namelist = []
index = 0

for el in col_one_list:
    tok = el.split()
    #print(tok)
    a = tok[0]
    b = a.replace(" ","")
    #print(' ' in b)
    namelist.append(b)
    indx = namelist.index(b)
    if tok[1] == "generalcovid":
        count_general[indx] = col_two_list[index]
    elif tok[1] == "fakecovid":
        count_fake[indx] = col_two_list[index]
    else:
        print("errore count")
    index = index + 1

df['Hashtag']=namelist
df['General Covid']=count_fake
df['Fake Covid']=count_general
del df['Count']

df_norm = df.copy()
df_norm[['General Covid', 'Fake Covid']] = (df_norm[['General Covid', 'Fake Covid']] - df_norm[['General Covid', 'Fake Covid']].min()) / (df_norm[['General Covid', 'Fake Covid']].max() - df_norm[['General Covid', 'Fake Covid']].min())
