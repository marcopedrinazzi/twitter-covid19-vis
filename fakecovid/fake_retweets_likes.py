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

#print(mix)
#print(dates)
#print(likes)
#print(retweets)
#print(category)

df_likes = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })
df_likes['Dates']= pd.to_datetime(df_likes['Dates'])

cl = df_likes['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes['Category'] = cl_cat

df_retweets = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })
df_retweets['Dates']= pd.to_datetime(df_retweets['Dates'])
cr = df_retweets['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets['Category'] = cr_cat

df = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })
df['Dates']= pd.to_datetime(df['Dates'])
df = df.sort_values(by=['Dates'], ascending=True)

#Normalizzare like e retweet
#https://www.geeksforgeeks.org/normalize-a-column-in-pandas/
#https://stackoverflow.com/a/41532180

df_norm = df.copy()
df_norm[['Likes', 'Retweets']] = (df_norm[['Likes', 'Retweets']] - df_norm[['Likes', 'Retweets']].min()) / (df_norm[['Likes', 'Retweets']].max() - df_norm[['Likes', 'Retweets']].min())
df_likes['Likes'] = df_norm['Likes']
df_retweets['Retweets'] = df_norm['Retweets']

c = alt.Chart(df_retweets).mark_line().encode(
    x="Dates",
    y="Retweets",
    color="Category"
)

#c.show()

c1 = alt.Chart(df_likes).mark_line().encode(
    x="Dates",
    y="Likes",
    color="Category"
)
#c1.show()

c2 = alt.layer(c,c1)
c2.show()

