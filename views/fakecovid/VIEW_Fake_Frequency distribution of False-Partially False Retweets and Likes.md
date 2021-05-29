# Frequency distribution of False-Partially False Retweets and Likes for each month until July 2020

We need the following packages:


```python
import pandas as pd
import datetime
from dateutil.parser import parse
import json
import itertools
import altair as alt
import csv
from vega_datasets import data
import pytz
utc=pytz.UTC
```

To read the JSON file that has all the tweets, it is necessary to do:


```python
csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))


data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
```

## January 2020

We're interested in the "retweet_count" and "favorite_count" fields:


```python
start = utc.localize(datetime.datetime(2020, 1, 1))
end = utc.localize(datetime.datetime(2020, 1, 31))

index=0
dates = ["2020-01-16"] 
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

# Fill the empty dates with 0.
start = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-01-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
```

We create the DataFrames which will be used to realize the chart, one for the Retweets count and one for the Likes count:


```python
df_likes_jan = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_jan['Dates']= pd.to_datetime(df_likes_jan['Dates'])
cl = df_likes_jan['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_jan['Category'] = cl_cat



df_retweets_jan = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_jan['Dates']= pd.to_datetime(df_retweets_jan['Dates'])
cr = df_retweets_jan['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_jan['Category'] = cr_cat



df_jan = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_jan['Dates']= pd.to_datetime(df_jan['Dates'])
df_jan = df_jan.sort_values(by=['Dates'], ascending=True)
```

We've normalised the count of Likes and Retweets using Min-Max Normalization in the scale of [0; 1].


```python
# Likes and Retweets normalization.
# https://www.geeksforgeeks.org/normalize-a-column-in-pandas/

df_norm_jan = df_jan.copy()
df_norm_jan[['Likes', 'Retweets']] = (df_norm_jan[['Likes', 'Retweets']] - df_norm_jan[['Likes', 'Retweets']].min()) / (df_norm_jan[['Likes', 'Retweets']].max() - df_norm_jan[['Likes', 'Retweets']].min())
df_likes_jan['Likes'] = df_norm_jan['Likes']
df_retweets_jan['Retweets'] = df_norm_jan['Retweets']
```

The line chart is created:


```python
c1_jan = alt.Chart(df_likes_jan).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#271a68', '#F09030'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_jan.encoding.x.title = 'Dates'

c2_jan = alt.Chart(df_retweets_jan).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#A8D8A8', '#FF90D8'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_jan.encoding.x.title = 'Dates'
```

We normalised the count of Retweets and Likes for the overall month together and plotted the normalised count of Retweets and Likes for both false and partially false and plotted it for each month, until August 2020.

## February 2020


```python
start = utc.localize(datetime.datetime(2020, 2, 1))
end = utc.localize(datetime.datetime(2020, 2, 29))

index=0
dates = ["2020-02-02"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-02-02 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-02-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-02-29", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_feb = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_feb['Dates']= pd.to_datetime(df_likes_feb['Dates'])
cl = df_likes_feb['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_feb['Category'] = cl_cat


df_retweets_feb = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_feb['Dates']= pd.to_datetime(df_retweets_feb['Dates'])
cr = df_retweets_feb['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_feb['Category'] = cr_cat


df_feb = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_feb['Dates']= pd.to_datetime(df_feb['Dates'])
df_feb = df_feb.sort_values(by=['Dates'], ascending=True)



df_norm_feb = df_feb.copy()
df_norm_feb[['Likes', 'Retweets']] = (df_norm_feb[['Likes', 'Retweets']] - df_norm_feb[['Likes', 'Retweets']].min()) / (df_norm_feb[['Likes', 'Retweets']].max() - df_norm_feb[['Likes', 'Retweets']].min())
df_likes_feb['Likes'] = df_norm_feb['Likes']
df_retweets_feb['Retweets'] = df_norm_feb['Retweets']



c1_feb = alt.Chart(df_likes_feb).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#5c44d0', '#e45700'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_feb.encoding.x.title = 'Dates'

c2_feb = alt.Chart(df_retweets_feb).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#00F0A8', '#FFC0C0'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_feb.encoding.x.title = 'Dates'
```

## March 2020


```python
start = utc.localize(datetime.datetime(2020, 3, 1))
end = utc.localize(datetime.datetime(2020, 3, 31))

index=0
dates = ["2020-03-04"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-03-04 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-03-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_mar = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_mar['Dates']= pd.to_datetime(df_likes_mar['Dates'])
cl = df_likes_mar['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_mar['Category'] = cl_cat


df_retweets_mar = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_mar['Dates']= pd.to_datetime(df_retweets_mar['Dates'])
cr = df_retweets_mar['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_mar['Category'] = cr_cat


df_mar = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_mar['Dates']= pd.to_datetime(df_mar['Dates'])
df_mar = df_mar.sort_values(by=['Dates'], ascending=True)



df_norm_mar = df_mar.copy()
df_norm_mar[['Likes', 'Retweets']] = (df_norm_mar[['Likes', 'Retweets']] - df_norm_mar[['Likes', 'Retweets']].min()) / (df_norm_mar[['Likes', 'Retweets']].max() - df_norm_mar[['Likes', 'Retweets']].min())
df_likes_mar['Likes'] = df_norm_mar['Likes']
df_retweets_mar['Retweets'] = df_norm_mar['Retweets']



c1_mar = alt.Chart(df_likes_mar).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#000090', '#985629'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_mar.encoding.x.title = 'Dates'

c2_mar = alt.Chart(df_retweets_mar).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#007848', '#C060A8'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_mar.encoding.x.title = 'Dates'
```

## April 2020


```python
start = utc.localize(datetime.datetime(2020, 4, 1))
end = utc.localize(datetime.datetime(2020, 4, 30))

index=0
dates = ["2020-04-08"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-04-08 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-04-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-04-30", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_apr = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_apr['Dates']= pd.to_datetime(df_likes_apr['Dates'])
cl = df_likes_apr['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_apr['Category'] = cl_cat


df_retweets_apr = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_apr['Dates']= pd.to_datetime(df_retweets_apr['Dates'])
cr = df_retweets_apr['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_apr['Category'] = cr_cat


df_apr = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_apr['Dates']= pd.to_datetime(df_apr['Dates'])
df_apr = df_apr.sort_values(by=['Dates'], ascending=True)



df_norm_apr = df_apr.copy()
df_norm_apr[['Likes', 'Retweets']] = (df_norm_apr[['Likes', 'Retweets']] - df_norm_apr[['Likes', 'Retweets']].min()) / (df_norm_apr[['Likes', 'Retweets']].max() - df_norm_apr[['Likes', 'Retweets']].min())
df_likes_apr['Likes'] = df_norm_apr['Likes']
df_retweets_apr['Retweets'] = df_norm_apr['Retweets']



c1_apr = alt.Chart(df_likes_apr).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#4890A8', '#FF8840'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_apr.encoding.x.title = 'Dates'

c2_apr = alt.Chart(df_retweets_apr).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#3CD070', '#904860'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_apr.encoding.x.title = 'Dates'
```

## May 2020


```python
start = utc.localize(datetime.datetime(2020, 5, 1))
end = utc.localize(datetime.datetime(2020, 5, 31))

index=0
dates = ["2020-05-03"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-05-03 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-05-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-05-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_may = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_may['Dates']= pd.to_datetime(df_likes_may['Dates'])
cl = df_likes_may['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_may['Category'] = cl_cat


df_retweets_may = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_may['Dates']= pd.to_datetime(df_retweets_may['Dates'])
cr = df_retweets_may['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_may['Category'] = cr_cat


df_may = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_may['Dates']= pd.to_datetime(df_may['Dates'])
df_may = df_may.sort_values(by=['Dates'], ascending=True)



df_norm_may = df_may.copy()
df_norm_may[['Likes', 'Retweets']] = (df_norm_may[['Likes', 'Retweets']] - df_norm_may[['Likes', 'Retweets']].min()) / (df_norm_may[['Likes', 'Retweets']].max() - df_norm_may[['Likes', 'Retweets']].min())
df_likes_may['Likes'] = df_norm_may['Likes']
df_retweets_may['Retweets'] = df_norm_may['Retweets']



c1_may = alt.Chart(df_likes_may).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#181041', '#FFA500'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_may.encoding.x.title = 'Dates'

c2_may = alt.Chart(df_retweets_may).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#00C0A8', '#D8A8A8'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_may.encoding.x.title = 'Dates'
```

## June 2020


```python
start = utc.localize(datetime.datetime(2020, 6, 1))
end = utc.localize(datetime.datetime(2020, 6, 30))

index=0
dates = ["2020-06-01"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-06-01 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-06-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-06-30", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_jun = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_jun['Dates']= pd.to_datetime(df_likes_jun['Dates'])
cl = df_likes_jun['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_jun['Category'] = cl_cat


df_retweets_jun = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_jun['Dates']= pd.to_datetime(df_retweets_jun['Dates'])
cr = df_retweets_jun['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_jun['Category'] = cr_cat


df_jun = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_jun['Dates']= pd.to_datetime(df_jun['Dates'])
df_jun = df_jun.sort_values(by=['Dates'], ascending=True)



df_norm_jun = df_jun.copy()
df_norm_jun[['Likes', 'Retweets']] = (df_norm_jun[['Likes', 'Retweets']] - df_norm_jun[['Likes', 'Retweets']].min()) / (df_norm_jun[['Likes', 'Retweets']].max() - df_norm_jun[['Likes', 'Retweets']].min())
df_likes_jun['Likes'] = df_norm_jun['Likes']
df_retweets_jun['Retweets'] = df_norm_jun['Retweets']



c1_jun = alt.Chart(df_likes_jun).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#007890', '#923800'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_jun.encoding.x.title = 'Dates'

c2_jun = alt.Chart(df_retweets_jun).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#00C000', '#FF007F'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_jun.encoding.x.title = 'Dates'
```

## July 2020


```python
start = utc.localize(datetime.datetime(2020, 7, 1))
end = utc.localize(datetime.datetime(2020, 7, 31))

index=0
dates = ["2020-07-01"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-07-01 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-07-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-07-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_jul = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_jul['Dates']= pd.to_datetime(df_likes_jul['Dates'])
cl = df_likes_jul['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_jul['Category'] = cl_cat


df_retweets_jul = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_jul['Dates']= pd.to_datetime(df_retweets_jul['Dates'])
cr = df_retweets_jul['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_jul['Category'] = cr_cat


df_jul = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_jul['Dates']= pd.to_datetime(df_jul['Dates'])
df_jul = df_jul.sort_values(by=['Dates'], ascending=True)



df_norm_jul = df_jul.copy()
df_norm_jul[['Likes', 'Retweets']] = (df_norm_jul[['Likes', 'Retweets']] - df_norm_jul[['Likes', 'Retweets']].min()) / (df_norm_jul[['Likes', 'Retweets']].max() - df_norm_jul[['Likes', 'Retweets']].min())
df_likes_jul['Likes'] = df_norm_jul['Likes']
df_retweets_jul['Retweets'] = df_norm_jul['Retweets']



c1_jul = alt.Chart(df_likes_jul).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#0030FF', '#E66C2C'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_jul.encoding.x.title = 'Dates'

c2_jul = alt.Chart(df_retweets_jul).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#00FF7F', '#DE5D83'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_jul.encoding.x.title = 'Dates'
```

## August 2020


```python
start = utc.localize(datetime.datetime(2020, 7, 1))
end = utc.localize(datetime.datetime(2020, 7, 31))

index=0
dates = ["2020-08-07"] 
retweets = [0]
likes = [0]
category = ["partially false"]
mix = ["2020-08-07 partially false"]
for element in data:
    token_id = data[index]['id_str']
    indice_csv = lista_unica_csv.index(token_id)
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        
        d = d.strftime('%Y-%m-%d')
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


start = datetime.datetime.strptime("2020-08-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-08-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        a = d + " " + "false"
        mix.append(a)
        dates.append(d)
        category.append("false")
        retweets.append(0)
        likes.append(0)
        a1 = d + " " + "partially false"
        mix.append(a1)
        dates.append(d)
        category.append("partially false")
        retweets.append(0)
        likes.append(0)
        

df_likes_aug = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Category': category
    })

df_likes_aug['Dates']= pd.to_datetime(df_likes_aug['Dates'])
cl = df_likes_aug['Category'].to_list()
cl_cat = [s + " likes" for s in cl]
df_likes_aug['Category'] = cl_cat


df_retweets_aug = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Category': category
    })

df_retweets_aug['Dates']= pd.to_datetime(df_retweets_aug['Dates'])
cr = df_retweets_aug['Category'].to_list()
cr_cat = [s + " retweets" for s in cr]
df_retweets_aug['Category'] = cr_cat


df_aug = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets,
     'Category': category
    })

df_aug['Dates']= pd.to_datetime(df_aug['Dates'])
df_aug = df_aug.sort_values(by=['Dates'], ascending=True)



df_norm_aug = df_aug.copy()
df_norm_aug[['Likes', 'Retweets']] = (df_norm_aug[['Likes', 'Retweets']] - df_norm_aug[['Likes', 'Retweets']].min()) / (df_norm_aug[['Likes', 'Retweets']].max() - df_norm_aug[['Likes', 'Retweets']].min())
df_likes_aug['Likes'] = df_norm_aug['Likes']
df_retweets_aug['Retweets'] = df_norm_aug['Retweets']



c1_aug = alt.Chart(df_likes_aug).mark_line().encode(
    x="monthdate(Dates):T",
    y="Likes",
    color=alt.Color('Category', scale=alt.Scale(range=['#0087FF', '#FF862E'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c1_aug.encoding.x.title = 'Dates'

c2_aug = alt.Chart(df_retweets_aug).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Category', scale=alt.Scale(range=['#008000', '#F791F5'])),
    row="Category"
).properties(
    width=250,
    height=110
)
c2_aug.encoding.x.title = 'Dates'
```

To summarize, below you can find every chart produced in this notebook.

## January 2020


```python
alt.hconcat(c1_jan, c2_jan).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## February 2020


```python
alt.hconcat(c1_feb, c2_feb).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## March 2020


```python
alt.hconcat(c1_mar, c2_mar).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## April 2020


```python
alt.hconcat(c1_apr, c2_apr).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## May 2020


```python
alt.hconcat(c1_may, c2_may).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## June 2020


```python
alt.hconcat(c1_jun, c2_jun).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## July 2020


```python
alt.hconcat(c1_jul, c2_jul).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

## August 2020


```python
alt.hconcat(c1_aug, c2_aug).resolve_scale(color='independent').configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    titleFontSize=15,
    titlePadding= 10,
    labelFontSize=12
).configure_header(
    titleFontSize=15,
    labelFontSize=12
)
```

# Recap

## January 2020

![january_fake.png](./img/january_fake.png)

## February 2020

![february_fake.png](./img/february_fake.png)

## March 2020

![march_fake.png](./img/march_fake.png)

## April 2020

![april_fake.png](./img/april_fake.png)

## May 2020

![may_fake.png](./img/may_fake.png)

## June 2020

![june_fake.png](./img/june_fake.png)

## July 2020

![july_fake.png](./img/july_fake.png)

## August

![august_fake.png](./img/august_fake.png)
