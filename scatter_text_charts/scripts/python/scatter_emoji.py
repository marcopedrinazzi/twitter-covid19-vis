import json
import pandas as pd
import csv
import itertools
import demoji
from collections import Counter
import nltk
import altair as alt

#csv_dataframe = pd.read_csv('twitter-covid19-vis/fakecovid/dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
#csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
#csv_list = csv_dataframe.values.tolist()
#lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('twitter-covid19-vis/fakecovid/dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

data1 = []
with open('general_result_translated_full.json', 'r') as f1:
    for line in f1:
        data1.append(json.loads(line))

index= 0
emos = []
for element in data:
    em = demoji.findall_list(data[index]['full_text'], False)
    for e in em:
        e = e + "  " + "fakecovid"
        emos.append(e)
    index= index+1

index1= 0
emos1 = []
for element in data1:
    em = demoji.findall_list(data1[index1]['full_text'], False)
    for e in em:
        e = e + "  " + "generalcovid"
        emos1.append(e)
    index1= index1+1

merged_final = emos + emos1

c = dict(nltk.FreqDist(merged_final))

df = pd.DataFrame.from_dict(c, orient='index').reset_index()
df = df.rename(columns={'index':'Emoji', 0:'Count'})

col_one_list = df['Emoji'].tolist()
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

df['Emoji']=namelist
df['General Covid']=count_fake
df['Fake Covid']=count_general
del df['Count']

df_norm = df.copy()
df_norm[['General Covid', 'Fake Covid']] = (df_norm[['General Covid', 'Fake Covid']] - df_norm[['General Covid', 'Fake Covid']].min()) / (df_norm[['General Covid', 'Fake Covid']].max() - df_norm[['General Covid', 'Fake Covid']].min())
#print(df_norm.to_string())


a = alt.Chart(df_norm).mark_text().encode(
    x=alt.X('General Covid', scale=alt.Scale(type="log")),
    y=alt.Y('Fake Covid'), #, scale=alt.Scale(type="log") ????
#    text="Emoji",
    #color=alt.Color('Emoji',legend=None,
    #tooltip=['Emoji', 'General Covid', 'Fake Covid']
).transform_filter(
    {"and": [alt.FieldGTPredicate(field='General Covid', gt=0), alt.FieldGTPredicate(field='Fake Covid', gt=0)]}
).properties(width=800,height=500)

#text = a.mark_text(
#    align='left',
#    baseline='middle',
#    dx=7
#).encode(
#    text='Emoji'
#)

#(a+text).show()

a.show()