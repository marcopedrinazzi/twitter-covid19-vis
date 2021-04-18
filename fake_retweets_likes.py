from collections import Counter
import pandas as pd
import datetime
from dateutil.parser import parse
import json
import itertools  
import nltk
import altair as alt
import csv
from vega_datasets import data


csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))


data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))


date_format = "%Y-%m-%d"
start = datetime.datetime.strptime("2020-01-01", date_format)
end = datetime.datetime.strptime("2020-01-31", date_format)


index=0
lista = [] 
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
    d = d.strftime('%Y-%m-%d')

    if start <= datetime.datetime.strptime(d, date_format) <= end:
        retweet = data[index]['retweet_count']
        likes = data[index]['favorite_count']
        final_token = str(retweet)+ " " +str(likes)+ " " +d+ " " +lista_unica_csv[indice_csv+1].lower().replace(" ", "")
        lista.append(final_token)
        #print(lista)

    index=index+1

fdist = dict(nltk.FreqDist(lista))
df = pd.DataFrame.from_dict(fdist, orient='index').reset_index()
df = df.rename(columns={'index':'Month', 0:'Count'})

col_one_list = df['Month'].tolist()
col_two_list = df['Count'].tolist()

typelist=[]
namelist=[]

index = 0

count_false_retweet = [0] * len(col_one_list)
count_part_retweet = [0] * len(col_one_list)

count_false_likes = [0] * len(col_one_list)
count_part_likes = [0] * len(col_one_list)


for el in col_one_list:
    tok = el.split()
    #print(tok)     ['503', '527', '2020-01-29', 'false']
    namelist.append(tok[2])
    if tok[2] in namelist:
        indx = namelist.index(tok[2])
        if tok[3] == "false":
            count_false_retweet[indx] = col_two_list[index]
            count_false_likes[indx] = col_two_list[index]
        elif tok[3] == "partiallyfalse":
            count_part_retweet[indx] = col_two_list[index]
            count_part_likes[indx] = col_two_list[index]
        else:
            print("errore")
   
    index = index + 1

i=0
for el in col_two_list:
    col_two_list[i] = count_false_retweet[i] + count_part_retweet[i] + count_false_likes[i] + count_part_likes[i]
    i = i + 1

df['Month']=namelist
df['False (Retweet)']=count_false_retweet
df['Partially False (Retweet)']=count_part_retweet
df['False (Likes)']=count_false_likes
df['Partially False (Likes)']=count_part_likes
df['Count'] = col_two_list

df = df.sort_values(by=['Count'],ascending=[False])

#print(df)

chart = alt.Chart(df).transform_fold(
    ['False (Retweet)',
     'Partially False (Retweet)',
     'False (Likes)',
     'Partially False (Likes)'],
    as_ = ['Category', 'Count']
).transform_density(
    density='Count',
    bandwidth=0.3,
    groupby=['Category'],
    extent= [0, 8],
    counts = True,
    steps=200
).mark_area().encode(
    alt.X('Month'),
    alt.Y('Count:Q', stack='zero'),
    alt.Color('Category:N')
).properties(width=400, height=100)

chart.show()
