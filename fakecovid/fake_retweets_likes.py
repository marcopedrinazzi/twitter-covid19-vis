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
import pytz
utc=pytz.UTC


csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))


data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))


#date_format = "%Y-%m-%d"
#start = datetime.datetime.strptime("2020-01-01", date_format)
#end = datetime.datetime.strptime("2020-01-31", date_format)
start = utc.localize(datetime.datetime(2020, 1, 1))
end = utc.localize(datetime.datetime(2020, 1, 31))

index=0
dates = ["2020-01-16"] 
lista = []
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-01-16 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
        #print(d)
        #print(lista_unica_csv[indice_csv+1].lower())
        #print(data[index]['retweet_count'])
        #print(data[index]['favorite_count'])
        #print(" ")
        a = d + " " + lista_unica_csv[indice_csv+1].lower()
        if a in mix:
            i = mix.index(a)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            mix.append(a)
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
            category.append(lista_unica_csv[indice_csv+1].lower())
        
       
    index=index+1

print(mix)
print(dates)
print(likes)
print(retweets)
print(category)

df = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })
df['Dates']= pd.to_datetime(df['Dates'])

#Normalizzare like e retweet
#https://www.geeksforgeeks.org/normalize-a-column-in-pandas/
#https://stackoverflow.com/a/41532180

#Plot
#chart = alt.Chart(df).transform_fold(
#    ['False (Retweet)',
#     'Partially False (Retweet)',
#     'False (Likes)',
#     'Partially False (Likes)'],
#    as_ = ['Category', 'Count']
#).transform_density(
#    density='Count',
#    bandwidth=0.3,
#    groupby=['Category'],
#    extent= [0, 8],
#    counts = True,
#    steps=200
#).mark_area().encode(
#    alt.X('Month'),
#    alt.Y('Count:Q', stack='zero'),
#    alt.Color('Category:N')
#).properties(width=400, height=100)

#chart.show()
