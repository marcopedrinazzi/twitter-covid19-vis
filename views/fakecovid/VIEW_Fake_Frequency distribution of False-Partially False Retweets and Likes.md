# Frequency distribution of False-Partially False Retweets and Likes for each month until August 2020

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
c1_jan.encoding.y.title = 'Norm. Count'

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
c2_jan.encoding.y.title = 'Norm. Count'
```

We normalised the count of Retweets and Likes for the overall month together and plotted the normalised count of Retweets and Likes for both false and partially false for each month, until August 2020.

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
c1_feb.encoding.y.title = 'Norm. Count'

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
c2_feb.encoding.y.title = 'Norm. Count'
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
c1_mar.encoding.y.title = 'Norm. Count'

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
c2_mar.encoding.y.title = 'Norm. Count'
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
c1_apr.encoding.y.title = 'Norm. Count'

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
c2_apr.encoding.y.title = 'Norm. Count'
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
c1_may.encoding.y.title = 'Norm. Count'

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
c2_may.encoding.y.title = 'Norm. Count'
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
c1_jun.encoding.y.title = 'Norm. Count'

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
c2_jun.encoding.y.title = 'Norm. Count'
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
c1_jul.encoding.y.title = 'Norm. Count'

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
c2_jul.encoding.y.title = 'Norm. Count'
```

## August 2020


```python
start = utc.localize(datetime.datetime(2020, 8, 1))
end = utc.localize(datetime.datetime(2020, 8, 31))

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
c1_aug.encoding.y.title = 'Norm. Count'

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
c2_aug.encoding.y.title = 'Norm. Count'
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





<div id="altair-viz-83b08f30b5b240b58b3f7b9cde944f5d"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-83b08f30b5b240b58b3f7b9cde944f5d") {
      outputDiv = document.getElementById("altair-viz-83b08f30b5b240b58b3f7b9cde944f5d");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-ba2da887cf692bb97179da50085b463d"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#271a68", "#F09030"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-cebf29455b794b7301603dabf0bbed37"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#A8D8A8", "#FF90D8"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-ba2da887cf692bb97179da50085b463d": [{"Dates": "2020-01-16T00:00:00", "Likes": 0.0002456278247199843, "Category": "partially false likes"}, {"Dates": "2020-01-27T00:00:00", "Likes": 0.12972424182878103, "Category": "false likes"}, {"Dates": "2020-01-16T00:00:00", "Likes": 0.0013263902534879151, "Category": "false likes"}, {"Dates": "2020-01-14T00:00:00", "Likes": 0.4420973341193424, "Category": "partially false likes"}, {"Dates": "2020-01-19T00:00:00", "Likes": 0.004061046702037073, "Category": "partially false likes"}, {"Dates": "2020-01-21T00:00:00", "Likes": 0.0012936398768585839, "Category": "partially false likes"}, {"Dates": "2020-01-29T00:00:00", "Likes": 0.02269601100412655, "Category": "false likes"}, {"Dates": "2020-01-19T00:00:00", "Likes": 0.00042575489618130606, "Category": "false likes"}, {"Dates": "2020-01-22T00:00:00", "Likes": 0.03155498788236065, "Category": "false likes"}, {"Dates": "2020-01-21T00:00:00", "Likes": 0.005092683565861007, "Category": "false likes"}, {"Dates": "2020-01-26T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-01-30T00:00:00", "Likes": 0.19766489814632868, "Category": "false likes"}, {"Dates": "2020-01-04T00:00:00", "Likes": 0.013018274710159167, "Category": "false likes"}, {"Dates": "2020-01-23T00:00:00", "Likes": 0.1288727320364184, "Category": "false likes"}, {"Dates": "2020-01-24T00:00:00", "Likes": 0.0006058819676426279, "Category": "false likes"}, {"Dates": "2020-01-24T00:00:00", "Likes": 0.26968297635422805, "Category": "partially false likes"}, {"Dates": "2020-01-25T00:00:00", "Likes": 0.21200956310997576, "Category": "false likes"}, {"Dates": "2020-01-25T00:00:00", "Likes": 0.08362808672299732, "Category": "partially false likes"}, {"Dates": "2020-01-26T00:00:00", "Likes": 0.0004912556494399686, "Category": "partially false likes"}, {"Dates": "2020-01-27T00:00:00", "Likes": 0.0013591406301172464, "Category": "partially false likes"}, {"Dates": "2020-01-28T00:00:00", "Likes": 0.12394380035370407, "Category": "false likes"}, {"Dates": "2020-01-29T00:00:00", "Likes": 0.056592650815484376, "Category": "partially false likes"}, {"Dates": "2020-01-15T00:00:00", "Likes": 0.0003602541429226436, "Category": "false likes"}, {"Dates": "2020-01-01T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-01T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-02T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-02T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-03T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-03T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-05T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-05T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-06T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-06T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-07T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-07T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-08T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-08T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-09T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-09T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-10T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-10T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-11T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-11T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-12T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-12T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-13T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-13T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-17T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-17T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-18T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-18T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-01-20T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-01-20T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-cebf29455b794b7301603dabf0bbed37": [{"Dates": "2020-01-16T00:00:00", "Retweets": 8.191685439279132e-05, "Category": "partially false retweets"}, {"Dates": "2020-01-27T00:00:00", "Retweets": 0.30038910505836575, "Category": "false retweets"}, {"Dates": "2020-01-16T00:00:00", "Retweets": 0.0015973786606594306, "Category": "false retweets"}, {"Dates": "2020-01-14T00:00:00", "Retweets": 0.9292647962318247, "Category": "partially false retweets"}, {"Dates": "2020-01-19T00:00:00", "Retweets": 0.0066762236330124925, "Category": "partially false retweets"}, {"Dates": "2020-01-21T00:00:00", "Retweets": 0.002744214622158509, "Category": "partially false retweets"}, {"Dates": "2020-01-29T00:00:00", "Retweets": 0.04509522834323162, "Category": "false retweets"}, {"Dates": "2020-01-19T00:00:00", "Retweets": 0.0007372516895351219, "Category": "false retweets"}, {"Dates": "2020-01-22T00:00:00", "Retweets": 0.028711857464673356, "Category": "false retweets"}, {"Dates": "2020-01-21T00:00:00", "Retweets": 0.010690149498259267, "Category": "false retweets"}, {"Dates": "2020-01-26T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-01-30T00:00:00", "Retweets": 0.2047511775547819, "Category": "false retweets"}, {"Dates": "2020-01-04T00:00:00", "Retweets": 0.018144583248003276, "Category": "false retweets"}, {"Dates": "2020-01-23T00:00:00", "Retweets": 0.4495187384804423, "Category": "false retweets"}, {"Dates": "2020-01-24T00:00:00", "Retweets": 0.0008601269711243088, "Category": "false retweets"}, {"Dates": "2020-01-24T00:00:00", "Retweets": 0.3379479827974606, "Category": "partially false retweets"}, {"Dates": "2020-01-25T00:00:00", "Retweets": 0.43350399344665164, "Category": "false retweets"}, {"Dates": "2020-01-25T00:00:00", "Retweets": 0.1406102805652263, "Category": "partially false retweets"}, {"Dates": "2020-01-26T00:00:00", "Retweets": 0.00036862584476756095, "Category": "partially false retweets"}, {"Dates": "2020-01-27T00:00:00", "Retweets": 0.003235715748515257, "Category": "partially false retweets"}, {"Dates": "2020-01-28T00:00:00", "Retweets": 0.13655539627278312, "Category": "false retweets"}, {"Dates": "2020-01-29T00:00:00", "Retweets": 0.031374155232439076, "Category": "partially false retweets"}, {"Dates": "2020-01-15T00:00:00", "Retweets": 0.00020479213598197828, "Category": "false retweets"}, {"Dates": "2020-01-01T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-01T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-02T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-02T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-03T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-03T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-05T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-05T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-06T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-06T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-07T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-07T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-08T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-08T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-09T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-09T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-10T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-10T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-11T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-11T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-12T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-12T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-13T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-13T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-17T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-17T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-18T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-18T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-01-20T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-01-20T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-7c468bdb4df84688afd9b495a7b11b75"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-7c468bdb4df84688afd9b495a7b11b75") {
      outputDiv = document.getElementById("altair-viz-7c468bdb4df84688afd9b495a7b11b75");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-ec7105a2cbf2400539ae2fc100104814"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#5c44d0", "#e45700"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-bafd4900f47e3a683a87cee3f1b9a04d"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#00F0A8", "#FFC0C0"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-ec7105a2cbf2400539ae2fc100104814": [{"Dates": "2020-02-02T00:00:00", "Likes": 0.0012780542592126412, "Category": "partially false likes"}, {"Dates": "2020-02-02T00:00:00", "Likes": 0.01343893418020565, "Category": "false likes"}, {"Dates": "2020-02-11T00:00:00", "Likes": 0.20795491954067505, "Category": "false likes"}, {"Dates": "2020-02-15T00:00:00", "Likes": 0.03235801010824732, "Category": "false likes"}, {"Dates": "2020-02-16T00:00:00", "Likes": 0.0022656416413315, "Category": "false likes"}, {"Dates": "2020-02-10T00:00:00", "Likes": 0.0064870935884278, "Category": "false likes"}, {"Dates": "2020-02-16T00:00:00", "Likes": 0.13698417923742762, "Category": "partially false likes"}, {"Dates": "2020-02-01T00:00:00", "Likes": 0.2813074882360915, "Category": "false likes"}, {"Dates": "2020-02-04T00:00:00", "Likes": 0.0014329699269959916, "Category": "false likes"}, {"Dates": "2020-02-26T00:00:00", "Likes": 0.0006777560465521581, "Category": "false likes"}, {"Dates": "2020-02-14T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-02-19T00:00:00", "Likes": 0.00023237350167502565, "Category": "false likes"}, {"Dates": "2020-02-22T00:00:00", "Likes": 0.007648961096802928, "Category": "false likes"}, {"Dates": "2020-02-23T00:00:00", "Likes": 0.00029046687709378206, "Category": "false likes"}, {"Dates": "2020-02-25T00:00:00", "Likes": 0.8143335721616545, "Category": "false likes"}, {"Dates": "2020-02-12T00:00:00", "Likes": 0.0003679247109854573, "Category": "false likes"}, {"Dates": "2020-02-08T00:00:00", "Likes": 0.0033887802327607908, "Category": "partially false likes"}, {"Dates": "2020-02-26T00:00:00", "Likes": 0.00939176235936562, "Category": "partially false likes"}, {"Dates": "2020-02-28T00:00:00", "Likes": 0.014213512519122402, "Category": "false likes"}, {"Dates": "2020-02-08T00:00:00", "Likes": 0.018841618094149998, "Category": "false likes"}, {"Dates": "2020-02-12T00:00:00", "Likes": 0.0012199608837938846, "Category": "partially false likes"}, {"Dates": "2020-02-25T00:00:00", "Likes": 0.000793942797389671, "Category": "partially false likes"}, {"Dates": "2020-02-06T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-02-07T00:00:00", "Likes": 0.1260626246587014, "Category": "false likes"}, {"Dates": "2020-02-03T00:00:00", "Likes": 0.0011425030499022095, "Category": "false likes"}, {"Dates": "2020-02-05T00:00:00", "Likes": 0.9210898317228559, "Category": "false likes"}, {"Dates": "2020-02-27T00:00:00", "Likes": 0.0003291957940396197, "Category": "false likes"}, {"Dates": "2020-02-05T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-02-07T00:00:00", "Likes": 0.007029298425669526, "Category": "partially false likes"}, {"Dates": "2020-02-09T00:00:00", "Likes": 0.06876319203733468, "Category": "false likes"}, {"Dates": "2020-02-09T00:00:00", "Likes": 3.872891694583761e-05, "Category": "partially false likes"}, {"Dates": "2020-02-11T00:00:00", "Likes": 0.049766658275401325, "Category": "partially false likes"}, {"Dates": "2020-02-18T00:00:00", "Likes": 0.012005964253209659, "Category": "partially false likes"}, {"Dates": "2020-02-18T00:00:00", "Likes": 0.019945392227106368, "Category": "false likes"}, {"Dates": "2020-02-20T00:00:00", "Likes": 0.02755562440696346, "Category": "partially false likes"}, {"Dates": "2020-02-28T00:00:00", "Likes": 0.3397106949904146, "Category": "partially false likes"}, {"Dates": "2020-02-13T00:00:00", "Likes": 0.25441025541720724, "Category": "partially false likes"}, {"Dates": "2020-02-17T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-02-17T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-02-21T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-02-21T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-02-24T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-02-24T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-bafd4900f47e3a683a87cee3f1b9a04d": [{"Dates": "2020-02-02T00:00:00", "Retweets": 0.002576529047297712, "Category": "partially false retweets"}, {"Dates": "2020-02-02T00:00:00", "Retweets": 0.02913931660634317, "Category": "false retweets"}, {"Dates": "2020-02-11T00:00:00", "Retweets": 0.6281823201030612, "Category": "false retweets"}, {"Dates": "2020-02-15T00:00:00", "Retweets": 0.030304889270596897, "Category": "false retweets"}, {"Dates": "2020-02-16T00:00:00", "Retweets": 0.0016563401018342434, "Category": "false retweets"}, {"Dates": "2020-02-10T00:00:00", "Retweets": 0.003987485430341697, "Category": "false retweets"}, {"Dates": "2020-02-16T00:00:00", "Retweets": 0.22967916078768175, "Category": "partially false retweets"}, {"Dates": "2020-02-01T00:00:00", "Retweets": 0.24317526532114594, "Category": "false retweets"}, {"Dates": "2020-02-04T00:00:00", "Retweets": 0.004355561008527084, "Category": "false retweets"}, {"Dates": "2020-02-26T00:00:00", "Retweets": 0.0007974970860683394, "Category": "false retweets"}, {"Dates": "2020-02-14T00:00:00", "Retweets": 6.134592969756457e-05, "Category": "false retweets"}, {"Dates": "2020-02-19T00:00:00", "Retweets": 0.00030672964848782285, "Category": "false retweets"}, {"Dates": "2020-02-22T00:00:00", "Retweets": 0.009815348751610331, "Category": "false retweets"}, {"Dates": "2020-02-23T00:00:00", "Retweets": 0.0001840377890926937, "Category": "false retweets"}, {"Dates": "2020-02-25T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-02-12T00:00:00", "Retweets": 0.0006134592969756457, "Category": "false retweets"}, {"Dates": "2020-02-08T00:00:00", "Retweets": 0.009815348751610331, "Category": "partially false retweets"}, {"Dates": "2020-02-26T00:00:00", "Retweets": 0.04337157229617815, "Category": "partially false retweets"}, {"Dates": "2020-02-28T00:00:00", "Retweets": 0.037052941537329, "Category": "false retweets"}, {"Dates": "2020-02-08T00:00:00", "Retweets": 0.04607079320287099, "Category": "false retweets"}, {"Dates": "2020-02-12T00:00:00", "Retweets": 0.0033126802036684867, "Category": "partially false retweets"}, {"Dates": "2020-02-25T00:00:00", "Retweets": 0.0015949941721366788, "Category": "partially false retweets"}, {"Dates": "2020-02-06T00:00:00", "Retweets": 0.8953438439359549, "Category": "false retweets"}, {"Dates": "2020-02-07T00:00:00", "Retweets": 0.2967302619471198, "Category": "false retweets"}, {"Dates": "2020-02-03T00:00:00", "Retweets": 0.0076068952824980066, "Category": "false retweets"}, {"Dates": "2020-02-05T00:00:00", "Retweets": 0.9039936200233114, "Category": "false retweets"}, {"Dates": "2020-02-27T00:00:00", "Retweets": 0.0007361511563707748, "Category": "false retweets"}, {"Dates": "2020-02-05T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-02-07T00:00:00", "Retweets": 0.013986871971044722, "Category": "partially false retweets"}, {"Dates": "2020-02-09T00:00:00", "Retweets": 0.09858290902398625, "Category": "false retweets"}, {"Dates": "2020-02-09T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-02-11T00:00:00", "Retweets": 0.07932028709895099, "Category": "partially false retweets"}, {"Dates": "2020-02-18T00:00:00", "Retweets": 0.026562787559045457, "Category": "partially false retweets"}, {"Dates": "2020-02-18T00:00:00", "Retweets": 0.0330654561069873, "Category": "false retweets"}, {"Dates": "2020-02-20T00:00:00", "Retweets": 0.06330899944788664, "Category": "partially false retweets"}, {"Dates": "2020-02-28T00:00:00", "Retweets": 0.338690877860254, "Category": "partially false retweets"}, {"Dates": "2020-02-13T00:00:00", "Retweets": 0.37697073799153424, "Category": "partially false retweets"}, {"Dates": "2020-02-17T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-02-17T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-02-21T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-02-21T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-02-24T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-02-24T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-f081f47ffbc54cb0bfb3de58e0209330"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-f081f47ffbc54cb0bfb3de58e0209330") {
      outputDiv = document.getElementById("altair-viz-f081f47ffbc54cb0bfb3de58e0209330");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-6dc3fb4e2fc04c99ea1f51202de53092"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#000090", "#985629"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-f447c5a940659948ac1af45dff3aea3f"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#007848", "#C060A8"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-6dc3fb4e2fc04c99ea1f51202de53092": [{"Dates": "2020-03-04T00:00:00", "Likes": 0.0005504901549757383, "Category": "partially false likes"}, {"Dates": "2020-03-11T00:00:00", "Likes": 0.060488295704353975, "Category": "false likes"}, {"Dates": "2020-03-24T00:00:00", "Likes": 0.3286845472674179, "Category": "false likes"}, {"Dates": "2020-03-26T00:00:00", "Likes": 0.020737255788349295, "Category": "false likes"}, {"Dates": "2020-03-27T00:00:00", "Likes": 0.00785997863660723, "Category": "partially false likes"}, {"Dates": "2020-03-15T00:00:00", "Likes": 0.10703205602604438, "Category": "false likes"}, {"Dates": "2020-03-20T00:00:00", "Likes": 0.01316254771218479, "Category": "false likes"}, {"Dates": "2020-03-23T00:00:00", "Likes": 0.24069088337264538, "Category": "false likes"}, {"Dates": "2020-03-27T00:00:00", "Likes": 0.3514478620201895, "Category": "false likes"}, {"Dates": "2020-03-05T00:00:00", "Likes": 0.022634806289441162, "Category": "false likes"}, {"Dates": "2020-03-06T00:00:00", "Likes": 0.001145639279477654, "Category": "false likes"}, {"Dates": "2020-03-18T00:00:00", "Likes": 0.13806365999394826, "Category": "false likes"}, {"Dates": "2020-03-22T00:00:00", "Likes": 0.05891976332568966, "Category": "false likes"}, {"Dates": "2020-03-28T00:00:00", "Likes": 0.3187702560326065, "Category": "false likes"}, {"Dates": "2020-03-07T00:00:00", "Likes": 0.0048286371540752675, "Category": "false likes"}, {"Dates": "2020-03-14T00:00:00", "Likes": 0.07668127349152938, "Category": "false likes"}, {"Dates": "2020-03-16T00:00:00", "Likes": 0.1580699669341344, "Category": "false likes"}, {"Dates": "2020-03-19T00:00:00", "Likes": 0.015545878432816504, "Category": "false likes"}, {"Dates": "2020-03-22T00:00:00", "Likes": 0.376514303629954, "Category": "partially false likes"}, {"Dates": "2020-03-30T00:00:00", "Likes": 0.00950051221103824, "Category": "partially false likes"}, {"Dates": "2020-03-30T00:00:00", "Likes": 0.06460968060634122, "Category": "false likes"}, {"Dates": "2020-03-21T00:00:00", "Likes": 0.28065701546840877, "Category": "false likes"}, {"Dates": "2020-03-23T00:00:00", "Likes": 0.0005997061622086686, "Category": "partially false likes"}, {"Dates": "2020-03-02T00:00:00", "Likes": 0.0015019996281457231, "Category": "false likes"}, {"Dates": "2020-03-03T00:00:00", "Likes": 0.03858443826307596, "Category": "false likes"}, {"Dates": "2020-03-17T00:00:00", "Likes": 0.14905979198034275, "Category": "false likes"}, {"Dates": "2020-03-20T00:00:00", "Likes": 0.011832804109354323, "Category": "partially false likes"}, {"Dates": "2020-03-21T00:00:00", "Likes": 0.004170600909220164, "Category": "partially false likes"}, {"Dates": "2020-03-25T00:00:00", "Likes": 0.12627824907674415, "Category": "false likes"}, {"Dates": "2020-03-28T00:00:00", "Likes": 0.00042653872935206216, "Category": "partially false likes"}, {"Dates": "2020-03-29T00:00:00", "Likes": 0.08351956427428263, "Category": "false likes"}, {"Dates": "2020-03-12T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-03-18T00:00:00", "Likes": 0.12904801659490853, "Category": "partially false likes"}, {"Dates": "2020-03-09T00:00:00", "Likes": 0.03916500486691627, "Category": "false likes"}, {"Dates": "2020-03-13T00:00:00", "Likes": 0.3355729654649454, "Category": "false likes"}, {"Dates": "2020-03-19T00:00:00", "Likes": 0.006018935403079099, "Category": "partially false likes"}, {"Dates": "2020-03-01T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-03-08T00:00:00", "Likes": 0.0042453363276109095, "Category": "false likes"}, {"Dates": "2020-03-16T00:00:00", "Likes": 0.009242583876836031, "Category": "partially false likes"}, {"Dates": "2020-03-24T00:00:00", "Likes": 0.0028399458988483455, "Category": "partially false likes"}, {"Dates": "2020-03-26T00:00:00", "Likes": 0.025253280155741322, "Category": "partially false likes"}, {"Dates": "2020-03-12T00:00:00", "Likes": 0.23436662644321385, "Category": "partially false likes"}, {"Dates": "2020-03-14T00:00:00", "Likes": 0.03364278657387323, "Category": "partially false likes"}, {"Dates": "2020-03-25T00:00:00", "Likes": 0.05601146186124002, "Category": "partially false likes"}, {"Dates": "2020-03-08T00:00:00", "Likes": 0.0012458941090262158, "Category": "partially false likes"}, {"Dates": "2020-03-09T00:00:00", "Likes": 0.02305405375846242, "Category": "partially false likes"}, {"Dates": "2020-03-13T00:00:00", "Likes": 0.0003199040470140466, "Category": "partially false likes"}, {"Dates": "2020-03-15T00:00:00", "Likes": 0.017790675207162935, "Category": "partially false likes"}, {"Dates": "2020-03-04T00:00:00", "Likes": 0.01829012653982304, "Category": "false likes"}, {"Dates": "2020-03-06T00:00:00", "Likes": 0.007470807616450542, "Category": "partially false likes"}, {"Dates": "2020-03-10T00:00:00", "Likes": 0.032995687219514326, "Category": "false likes"}, {"Dates": "2020-03-11T00:00:00", "Likes": 0.006063594372605277, "Category": "partially false likes"}, {"Dates": "2020-03-17T00:00:00", "Likes": 0.03410578160487931, "Category": "partially false likes"}, {"Dates": "2020-03-03T00:00:00", "Likes": 0.00028344774536002423, "Category": "partially false likes"}, {"Dates": "2020-03-05T00:00:00", "Likes": 0.0006425423166521449, "Category": "partially false likes"}, {"Dates": "2020-03-02T00:00:00", "Likes": 0.006533880663942166, "Category": "partially false likes"}], "data-f447c5a940659948ac1af45dff3aea3f": [{"Dates": "2020-03-04T00:00:00", "Retweets": 0.0012264702104473717, "Category": "partially false retweets"}, {"Dates": "2020-03-11T00:00:00", "Retweets": 0.21751200573457694, "Category": "false retweets"}, {"Dates": "2020-03-24T00:00:00", "Retweets": 0.45137004180771767, "Category": "false retweets"}, {"Dates": "2020-03-26T00:00:00", "Retweets": 0.029107950095921573, "Category": "false retweets"}, {"Dates": "2020-03-27T00:00:00", "Retweets": 0.00507576353985821, "Category": "partially false retweets"}, {"Dates": "2020-03-15T00:00:00", "Retweets": 0.18981283898849355, "Category": "false retweets"}, {"Dates": "2020-03-20T00:00:00", "Retweets": 0.03792527647373241, "Category": "false retweets"}, {"Dates": "2020-03-23T00:00:00", "Retweets": 0.5467902528766113, "Category": "false retweets"}, {"Dates": "2020-03-27T00:00:00", "Retweets": 0.5998848112437485, "Category": "false retweets"}, {"Dates": "2020-03-05T00:00:00", "Retweets": 0.02744641443920064, "Category": "false retweets"}, {"Dates": "2020-03-06T00:00:00", "Retweets": 0.003447375726662882, "Category": "false retweets"}, {"Dates": "2020-03-18T00:00:00", "Retweets": 0.24848866550925447, "Category": "false retweets"}, {"Dates": "2020-03-22T00:00:00", "Retweets": 0.09912862606332067, "Category": "false retweets"}, {"Dates": "2020-03-28T00:00:00", "Retweets": 0.36693419738712124, "Category": "false retweets"}, {"Dates": "2020-03-07T00:00:00", "Retweets": 0.01765122667738447, "Category": "false retweets"}, {"Dates": "2020-03-14T00:00:00", "Retweets": 0.2608901024682713, "Category": "false retweets"}, {"Dates": "2020-03-16T00:00:00", "Retweets": 0.3320626659981852, "Category": "false retweets"}, {"Dates": "2020-03-19T00:00:00", "Retweets": 0.0150159731170989, "Category": "false retweets"}, {"Dates": "2020-03-22T00:00:00", "Retweets": 0.5677023986608272, "Category": "partially false retweets"}, {"Dates": "2020-03-30T00:00:00", "Retweets": 0.015844669205239015, "Category": "partially false retweets"}, {"Dates": "2020-03-30T00:00:00", "Retweets": 0.0707872198489287, "Category": "false retweets"}, {"Dates": "2020-03-21T00:00:00", "Retweets": 0.6044136353654342, "Category": "false retweets"}, {"Dates": "2020-03-23T00:00:00", "Retweets": 0.000700248194478398, "Category": "partially false retweets"}, {"Dates": "2020-03-02T00:00:00", "Retweets": 0.005527402907894574, "Category": "false retweets"}, {"Dates": "2020-03-03T00:00:00", "Retweets": 0.06972648885610935, "Category": "false retweets"}, {"Dates": "2020-03-17T00:00:00", "Retweets": 0.18765408567888855, "Category": "false retweets"}, {"Dates": "2020-03-20T00:00:00", "Retweets": 0.033044256514587124, "Category": "partially false retweets"}, {"Dates": "2020-03-21T00:00:00", "Retweets": 0.008630869757979307, "Category": "partially false retweets"}, {"Dates": "2020-03-25T00:00:00", "Retweets": 0.1164235134228049, "Category": "false retweets"}, {"Dates": "2020-03-28T00:00:00", "Retweets": 0.0008162656468180142, "Category": "partially false retweets"}, {"Dates": "2020-03-29T00:00:00", "Retweets": 0.09677512917300274, "Category": "false retweets"}, {"Dates": "2020-03-12T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-03-18T00:00:00", "Retweets": 0.13487857530568528, "Category": "partially false retweets"}, {"Dates": "2020-03-09T00:00:00", "Retweets": 0.07189352912659576, "Category": "false retweets"}, {"Dates": "2020-03-13T00:00:00", "Retweets": 0.39419829868693107, "Category": "false retweets"}, {"Dates": "2020-03-19T00:00:00", "Retweets": 0.010188818403682725, "Category": "partially false retweets"}, {"Dates": "2020-03-01T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-03-08T00:00:00", "Retweets": 0.010503722917175969, "Category": "false retweets"}, {"Dates": "2020-03-16T00:00:00", "Retweets": 0.028080366946627827, "Category": "partially false retweets"}, {"Dates": "2020-03-24T00:00:00", "Retweets": 0.00636024247647539, "Category": "partially false retweets"}, {"Dates": "2020-03-26T00:00:00", "Retweets": 0.043568696833966594, "Category": "partially false retweets"}, {"Dates": "2020-03-12T00:00:00", "Retweets": 0.24137016611213086, "Category": "partially false retweets"}, {"Dates": "2020-03-14T00:00:00", "Retweets": 0.054420472108161415, "Category": "partially false retweets"}, {"Dates": "2020-03-25T00:00:00", "Retweets": 0.05200067953079227, "Category": "partially false retweets"}, {"Dates": "2020-03-08T00:00:00", "Retweets": 0.0013963529085160953, "Category": "partially false retweets"}, {"Dates": "2020-03-09T00:00:00", "Retweets": 0.04412392321302047, "Category": "partially false retweets"}, {"Dates": "2020-03-13T00:00:00", "Retweets": 0.0003977741223072556, "Category": "partially false retweets"}, {"Dates": "2020-03-15T00:00:00", "Retweets": 0.017348752605213326, "Category": "partially false retweets"}, {"Dates": "2020-03-04T00:00:00", "Retweets": 0.015272868904422336, "Category": "false retweets"}, {"Dates": "2020-03-06T00:00:00", "Retweets": 0.019896993076244183, "Category": "partially false retweets"}, {"Dates": "2020-03-10T00:00:00", "Retweets": 0.07091566774259042, "Category": "false retweets"}, {"Dates": "2020-03-11T00:00:00", "Retweets": 0.01044571419100616, "Category": "partially false retweets"}, {"Dates": "2020-03-17T00:00:00", "Retweets": 0.05132529221895808, "Category": "partially false retweets"}, {"Dates": "2020-03-03T00:00:00", "Retweets": 0.0001988870611536278, "Category": "partially false retweets"}, {"Dates": "2020-03-05T00:00:00", "Retweets": 0.0008452700099029183, "Category": "partially false retweets"}, {"Dates": "2020-03-02T00:00:00", "Retweets": 0.007686156217499575, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-b12891ea2ca344f2a0856f3b45f80a87"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-b12891ea2ca344f2a0856f3b45f80a87") {
      outputDiv = document.getElementById("altair-viz-b12891ea2ca344f2a0856f3b45f80a87");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-fd59b09852876269740c52a0fdc183c4"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#4890A8", "#FF8840"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-4dfaca85883944cb7da07a4341e0461f"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#3CD070", "#904860"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-fd59b09852876269740c52a0fdc183c4": [{"Dates": "2020-04-08T00:00:00", "Likes": 0.0008459874652119028, "Category": "partially false likes"}, {"Dates": "2020-04-08T00:00:00", "Likes": 0.06269165750057211, "Category": "false likes"}, {"Dates": "2020-04-09T00:00:00", "Likes": 0.02826306814406886, "Category": "false likes"}, {"Dates": "2020-04-15T00:00:00", "Likes": 0.6048795612085957, "Category": "false likes"}, {"Dates": "2020-04-21T00:00:00", "Likes": 0.014564862730044367, "Category": "false likes"}, {"Dates": "2020-04-24T00:00:00", "Likes": 0.017864656769745243, "Category": "false likes"}, {"Dates": "2020-04-28T00:00:00", "Likes": 0.009496320028347225, "Category": "false likes"}, {"Dates": "2020-04-12T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-04-15T00:00:00", "Likes": 0.018158463934801385, "Category": "partially false likes"}, {"Dates": "2020-04-26T00:00:00", "Likes": 0.1253316403741243, "Category": "false likes"}, {"Dates": "2020-04-29T00:00:00", "Likes": 0.04237171773842304, "Category": "false likes"}, {"Dates": "2020-04-01T00:00:00", "Likes": 0.0384739744432059, "Category": "false likes"}, {"Dates": "2020-04-03T00:00:00", "Likes": 0.007382089574274895, "Category": "false likes"}, {"Dates": "2020-04-12T00:00:00", "Likes": 0.0041073946391265515, "Category": "false likes"}, {"Dates": "2020-04-17T00:00:00", "Likes": 0.0506042240316544, "Category": "false likes"}, {"Dates": "2020-04-18T00:00:00", "Likes": 0.004684674043834848, "Category": "false likes"}, {"Dates": "2020-04-19T00:00:00", "Likes": 0.009381159430988535, "Category": "false likes"}, {"Dates": "2020-04-20T00:00:00", "Likes": 0.06500225153732016, "Category": "false likes"}, {"Dates": "2020-04-20T00:00:00", "Likes": 0.0004547367177753335, "Category": "partially false likes"}, {"Dates": "2020-04-06T00:00:00", "Likes": 0.14228091803665946, "Category": "false likes"}, {"Dates": "2020-04-07T00:00:00", "Likes": 0.08014439367207282, "Category": "false likes"}, {"Dates": "2020-04-10T00:00:00", "Likes": 0.06335899839808656, "Category": "partially false likes"}, {"Dates": "2020-04-22T00:00:00", "Likes": 0.02511386873168319, "Category": "false likes"}, {"Dates": "2020-04-25T00:00:00", "Likes": 0.0036615164288403474, "Category": "false likes"}, {"Dates": "2020-04-02T00:00:00", "Likes": 0.08951226534182766, "Category": "false likes"}, {"Dates": "2020-04-04T00:00:00", "Likes": 0.04398101326561497, "Category": "false likes"}, {"Dates": "2020-04-05T00:00:00", "Likes": 0.1907059492259879, "Category": "false likes"}, {"Dates": "2020-04-14T00:00:00", "Likes": 0.05762016196304526, "Category": "false likes"}, {"Dates": "2020-04-18T00:00:00", "Likes": 0.023331832308453232, "Category": "partially false likes"}, {"Dates": "2020-04-19T00:00:00", "Likes": 0.0031211474720034254, "Category": "partially false likes"}, {"Dates": "2020-04-22T00:00:00", "Likes": 0.0013597808995814355, "Category": "partially false likes"}, {"Dates": "2020-04-23T00:00:00", "Likes": 0.025850601271195824, "Category": "false likes"}, {"Dates": "2020-04-26T00:00:00", "Likes": 0.032498911141787795, "Category": "partially false likes"}, {"Dates": "2020-04-27T00:00:00", "Likes": 0.00017717014978259747, "Category": "false likes"}, {"Dates": "2020-04-27T00:00:00", "Likes": 0.008515978532883517, "Category": "partially false likes"}, {"Dates": "2020-04-03T00:00:00", "Likes": 0.07686674590109477, "Category": "partially false likes"}, {"Dates": "2020-04-04T00:00:00", "Likes": 0.000984770749208271, "Category": "partially false likes"}, {"Dates": "2020-04-10T00:00:00", "Likes": 0.02561732724064874, "Category": "false likes"}, {"Dates": "2020-04-11T00:00:00", "Likes": 0.2640396270568347, "Category": "false likes"}, {"Dates": "2020-04-13T00:00:00", "Likes": 1.0, "Category": "partially false likes"}, {"Dates": "2020-04-13T00:00:00", "Likes": 0.07051519603138864, "Category": "false likes"}, {"Dates": "2020-04-16T00:00:00", "Likes": 0.0046654806109417335, "Category": "false likes"}, {"Dates": "2020-04-16T00:00:00", "Likes": 0.0007145862707898098, "Category": "partially false likes"}, {"Dates": "2020-04-21T00:00:00", "Likes": 0.0051777976273964105, "Category": "partially false likes"}, {"Dates": "2020-04-05T00:00:00", "Likes": 0.01661560721377793, "Category": "partially false likes"}, {"Dates": "2020-04-07T00:00:00", "Likes": 0.007658179724352775, "Category": "partially false likes"}, {"Dates": "2020-04-01T00:00:00", "Likes": 0.44712283058842633, "Category": "partially false likes"}, {"Dates": "2020-04-02T00:00:00", "Likes": 0.004306711057631973, "Category": "partially false likes"}, {"Dates": "2020-04-06T00:00:00", "Likes": 0.0022087212006230484, "Category": "partially false likes"}, {"Dates": "2020-04-14T00:00:00", "Likes": 0.18051423635974398, "Category": "partially false likes"}, {"Dates": "2020-04-09T00:00:00", "Likes": 0.057324878380074266, "Category": "partially false likes"}], "data-4dfaca85883944cb7da07a4341e0461f": [{"Dates": "2020-04-08T00:00:00", "Retweets": 0.0012211914092922697, "Category": "partially false retweets"}, {"Dates": "2020-04-08T00:00:00", "Retweets": 0.07763288244786572, "Category": "false retweets"}, {"Dates": "2020-04-09T00:00:00", "Retweets": 0.06694745761655836, "Category": "false retweets"}, {"Dates": "2020-04-15T00:00:00", "Retweets": 0.6726085520782061, "Category": "false retweets"}, {"Dates": "2020-04-21T00:00:00", "Retweets": 0.04016847456993502, "Category": "false retweets"}, {"Dates": "2020-04-24T00:00:00", "Retweets": 0.027489267845905583, "Category": "false retweets"}, {"Dates": "2020-04-28T00:00:00", "Retweets": 0.011806927145963526, "Category": "false retweets"}, {"Dates": "2020-04-12T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-04-15T00:00:00", "Retweets": 0.022037520482993664, "Category": "partially false retweets"}, {"Dates": "2020-04-26T00:00:00", "Retweets": 0.206038666907582, "Category": "false retweets"}, {"Dates": "2020-04-29T00:00:00", "Retweets": 0.16620041246362904, "Category": "false retweets"}, {"Dates": "2020-04-01T00:00:00", "Retweets": 0.05439286226082406, "Category": "false retweets"}, {"Dates": "2020-04-03T00:00:00", "Retweets": 0.02533349117439984, "Category": "false retweets"}, {"Dates": "2020-04-12T00:00:00", "Retweets": 0.012168300114019402, "Category": "false retweets"}, {"Dates": "2020-04-17T00:00:00", "Retweets": 0.055564209122798275, "Category": "false retweets"}, {"Dates": "2020-04-18T00:00:00", "Retweets": 0.01087857245216481, "Category": "false retweets"}, {"Dates": "2020-04-19T00:00:00", "Retweets": 0.024405136480601126, "Category": "false retweets"}, {"Dates": "2020-04-20T00:00:00", "Retweets": 0.09327160916890448, "Category": "false retweets"}, {"Dates": "2020-04-20T00:00:00", "Retweets": 0.0007476682097707774, "Category": "partially false retweets"}, {"Dates": "2020-04-06T00:00:00", "Retweets": 0.19097938304911558, "Category": "false retweets"}, {"Dates": "2020-04-07T00:00:00", "Retweets": 0.10649910591343248, "Category": "false retweets"}, {"Dates": "2020-04-10T00:00:00", "Retweets": 0.13792609299746417, "Category": "partially false retweets"}, {"Dates": "2020-04-22T00:00:00", "Retweets": 0.03345192181882753, "Category": "false retweets"}, {"Dates": "2020-04-25T00:00:00", "Retweets": 0.012523442513660521, "Category": "false retweets"}, {"Dates": "2020-04-02T00:00:00", "Retweets": 0.09067969270836579, "Category": "false retweets"}, {"Dates": "2020-04-04T00:00:00", "Retweets": 0.07631200194393735, "Category": "false retweets"}, {"Dates": "2020-04-05T00:00:00", "Retweets": 0.11961445242649486, "Category": "false retweets"}, {"Dates": "2020-04-14T00:00:00", "Retweets": 0.07502227428208276, "Category": "false retweets"}, {"Dates": "2020-04-18T00:00:00", "Retweets": 0.04147066336861912, "Category": "partially false retweets"}, {"Dates": "2020-04-19T00:00:00", "Retweets": 0.002959519997009327, "Category": "partially false retweets"}, {"Dates": "2020-04-22T00:00:00", "Retweets": 0.004286631069352457, "Category": "partially false retweets"}, {"Dates": "2020-04-23T00:00:00", "Retweets": 0.03786316425647512, "Category": "false retweets"}, {"Dates": "2020-04-26T00:00:00", "Retweets": 0.028585847886902722, "Category": "partially false retweets"}, {"Dates": "2020-04-27T00:00:00", "Retweets": 0.000560751157328083, "Category": "false retweets"}, {"Dates": "2020-04-27T00:00:00", "Retweets": 0.007700982560639007, "Category": "partially false retweets"}, {"Dates": "2020-04-03T00:00:00", "Retweets": 0.07600670409161428, "Category": "partially false retweets"}, {"Dates": "2020-04-04T00:00:00", "Retweets": 0.003009364544327379, "Category": "partially false retweets"}, {"Dates": "2020-04-10T00:00:00", "Retweets": 0.04046131128542857, "Category": "false retweets"}, {"Dates": "2020-04-11T00:00:00", "Retweets": 0.2762571729418875, "Category": "false retweets"}, {"Dates": "2020-04-13T00:00:00", "Retweets": 1.0, "Category": "partially false retweets"}, {"Dates": "2020-04-13T00:00:00", "Retweets": 0.03888497747649518, "Category": "false retweets"}, {"Dates": "2020-04-16T00:00:00", "Retweets": 0.008523417591386862, "Category": "false retweets"}, {"Dates": "2020-04-16T00:00:00", "Retweets": 0.0040872528800802495, "Category": "partially false retweets"}, {"Dates": "2020-04-21T00:00:00", "Retweets": 0.0030841313653044568, "Category": "partially false retweets"}, {"Dates": "2020-04-05T00:00:00", "Retweets": 0.01924622583318276, "Category": "partially false retweets"}, {"Dates": "2020-04-07T00:00:00", "Retweets": 0.005619972710110344, "Category": "partially false retweets"}, {"Dates": "2020-04-01T00:00:00", "Retweets": 0.6672191103994417, "Category": "partially false retweets"}, {"Dates": "2020-04-02T00:00:00", "Retweets": 0.019395759475136918, "Category": "partially false retweets"}, {"Dates": "2020-04-06T00:00:00", "Retweets": 0.002591916460538695, "Category": "partially false retweets"}, {"Dates": "2020-04-14T00:00:00", "Retweets": 0.1422002629299871, "Category": "partially false retweets"}, {"Dates": "2020-04-09T00:00:00", "Retweets": 0.19623798279117005, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-f62da2c76bd347a690cb850f8fabf44b"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-f62da2c76bd347a690cb850f8fabf44b") {
      outputDiv = document.getElementById("altair-viz-f62da2c76bd347a690cb850f8fabf44b");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-92dd0b4eebd41b7327faff0930dc688b"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#181041", "#FFA500"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-8a5dcdbb59715418101fe8d801f15002"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#00C0A8", "#D8A8A8"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-92dd0b4eebd41b7327faff0930dc688b": [{"Dates": "2020-05-03T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-05-03T00:00:00", "Likes": 0.050933771510208635, "Category": "false likes"}, {"Dates": "2020-05-06T00:00:00", "Likes": 0.0037089155551360653, "Category": "partially false likes"}, {"Dates": "2020-05-07T00:00:00", "Likes": 0.0033978728972443766, "Category": "false likes"}, {"Dates": "2020-05-10T00:00:00", "Likes": 0.03934582366240932, "Category": "false likes"}, {"Dates": "2020-05-16T00:00:00", "Likes": 0.1088584948967553, "Category": "false likes"}, {"Dates": "2020-05-19T00:00:00", "Likes": 0.049805437454684305, "Category": "partially false likes"}, {"Dates": "2020-05-20T00:00:00", "Likes": 0.15988879688699928, "Category": "false likes"}, {"Dates": "2020-05-21T00:00:00", "Likes": 0.25845928773376464, "Category": "false likes"}, {"Dates": "2020-05-24T00:00:00", "Likes": 0.0018877071651357648, "Category": "false likes"}, {"Dates": "2020-05-25T00:00:00", "Likes": 0.08241128848884752, "Category": "false likes"}, {"Dates": "2020-05-26T00:00:00", "Likes": 0.000761518231389996, "Category": "partially false likes"}, {"Dates": "2020-05-26T00:00:00", "Likes": 0.014509603710202629, "Category": "false likes"}, {"Dates": "2020-05-27T00:00:00", "Likes": 0.0033099229043232785, "Category": "partially false likes"}, {"Dates": "2020-05-27T00:00:00", "Likes": 0.0888123318760806, "Category": "false likes"}, {"Dates": "2020-05-02T00:00:00", "Likes": 0.0012291547791168104, "Category": "partially false likes"}, {"Dates": "2020-05-06T00:00:00", "Likes": 0.021715067764396984, "Category": "false likes"}, {"Dates": "2020-05-11T00:00:00", "Likes": 0.05720396246894936, "Category": "false likes"}, {"Dates": "2020-05-12T00:00:00", "Likes": 0.211824340267797, "Category": "false likes"}, {"Dates": "2020-05-13T00:00:00", "Likes": 0.04377550013514267, "Category": "false likes"}, {"Dates": "2020-05-14T00:00:00", "Likes": 0.047265613268865275, "Category": "false likes"}, {"Dates": "2020-05-18T00:00:00", "Likes": 0.05548357480254154, "Category": "false likes"}, {"Dates": "2020-05-18T00:00:00", "Likes": 0.001128334055524332, "Category": "partially false likes"}, {"Dates": "2020-05-19T00:00:00", "Likes": 0.005058197153852424, "Category": "false likes"}, {"Dates": "2020-05-20T00:00:00", "Likes": 0.0005019584961838283, "Category": "partially false likes"}, {"Dates": "2020-05-22T00:00:00", "Likes": 0.0006993096998116583, "Category": "false likes"}, {"Dates": "2020-05-25T00:00:00", "Likes": 0.0004376048428269273, "Category": "partially false likes"}, {"Dates": "2020-05-28T00:00:00", "Likes": 0.00037754143302715294, "Category": "false likes"}, {"Dates": "2020-05-29T00:00:00", "Likes": 0.2030100348796801, "Category": "false likes"}, {"Dates": "2020-05-01T00:00:00", "Likes": 0.004736428887067919, "Category": "false likes"}, {"Dates": "2020-05-02T00:00:00", "Likes": 0.1844482961297713, "Category": "false likes"}, {"Dates": "2020-05-04T00:00:00", "Likes": 0.005403561760201126, "Category": "false likes"}, {"Dates": "2020-05-08T00:00:00", "Likes": 0.8331395573326698, "Category": "false likes"}, {"Dates": "2020-05-08T00:00:00", "Likes": 0.000482652400176758, "Category": "partially false likes"}, {"Dates": "2020-05-09T00:00:00", "Likes": 0.0010854316199530648, "Category": "false likes"}, {"Dates": "2020-05-11T00:00:00", "Likes": 1.0, "Category": "partially false likes"}, {"Dates": "2020-05-12T00:00:00", "Likes": 0.3659792266406964, "Category": "partially false likes"}, {"Dates": "2020-05-15T00:00:00", "Likes": 0.0029667034197531396, "Category": "partially false likes"}, {"Dates": "2020-05-17T00:00:00", "Likes": 0.049354961881185995, "Category": "false likes"}, {"Dates": "2020-05-21T00:00:00", "Likes": 0.0025248083333690853, "Category": "partially false likes"}, {"Dates": "2020-05-05T00:00:00", "Likes": 0.012984422125644072, "Category": "false likes"}, {"Dates": "2020-05-15T00:00:00", "Likes": 4.290243557126738e-06, "Category": "false likes"}, {"Dates": "2020-05-23T00:00:00", "Likes": 2.7886583121323797e-05, "Category": "partially false likes"}, {"Dates": "2020-05-04T00:00:00", "Likes": 7.722438402828128e-05, "Category": "partially false likes"}, {"Dates": "2020-05-07T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-05-22T00:00:00", "Likes": 2.145121778563369e-06, "Category": "partially false likes"}, {"Dates": "2020-05-01T00:00:00", "Likes": 0.00025097924809191417, "Category": "partially false likes"}, {"Dates": "2020-05-13T00:00:00", "Likes": 0.38959916254445764, "Category": "partially false likes"}, {"Dates": "2020-05-14T00:00:00", "Likes": 0.0026899827103184647, "Category": "partially false likes"}, {"Dates": "2020-05-30T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-05-30T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-8a5dcdbb59715418101fe8d801f15002": [{"Dates": "2020-05-03T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-05-03T00:00:00", "Retweets": 0.10697741638586108, "Category": "false retweets"}, {"Dates": "2020-05-06T00:00:00", "Retweets": 0.006389436132261328, "Category": "partially false retweets"}, {"Dates": "2020-05-07T00:00:00", "Retweets": 0.005096335962637011, "Category": "false retweets"}, {"Dates": "2020-05-10T00:00:00", "Retweets": 0.05737561517338952, "Category": "false retweets"}, {"Dates": "2020-05-16T00:00:00", "Retweets": 0.127621380270334, "Category": "false retweets"}, {"Dates": "2020-05-19T00:00:00", "Retweets": 0.07669605300189401, "Category": "partially false retweets"}, {"Dates": "2020-05-20T00:00:00", "Retweets": 0.08510120410445207, "Category": "false retweets"}, {"Dates": "2020-05-21T00:00:00", "Retweets": 0.10188868689481011, "Category": "false retweets"}, {"Dates": "2020-05-24T00:00:00", "Retweets": 0.0015365072603771288, "Category": "false retweets"}, {"Dates": "2020-05-25T00:00:00", "Retweets": 0.05957388546175086, "Category": "false retweets"}, {"Dates": "2020-05-26T00:00:00", "Retweets": 0.0008975636471509961, "Category": "partially false retweets"}, {"Dates": "2020-05-26T00:00:00", "Retweets": 0.022233716445952217, "Category": "false retweets"}, {"Dates": "2020-05-27T00:00:00", "Retweets": 0.012931001696243163, "Category": "partially false retweets"}, {"Dates": "2020-05-27T00:00:00", "Retweets": 0.13226132793780948, "Category": "false retweets"}, {"Dates": "2020-05-02T00:00:00", "Retweets": 0.0033924863273673243, "Category": "partially false retweets"}, {"Dates": "2020-05-06T00:00:00", "Retweets": 0.02716271003369667, "Category": "false retweets"}, {"Dates": "2020-05-11T00:00:00", "Retweets": 0.07771532019442141, "Category": "false retweets"}, {"Dates": "2020-05-12T00:00:00", "Retweets": 0.24881529205047653, "Category": "false retweets"}, {"Dates": "2020-05-13T00:00:00", "Retweets": 0.06757589357024957, "Category": "false retweets"}, {"Dates": "2020-05-14T00:00:00", "Retweets": 0.03446492275628105, "Category": "false retweets"}, {"Dates": "2020-05-18T00:00:00", "Retweets": 0.04542584831174363, "Category": "false retweets"}, {"Dates": "2020-05-18T00:00:00", "Retweets": 0.002669871526694912, "Category": "partially false retweets"}, {"Dates": "2020-05-19T00:00:00", "Retweets": 0.0039781846394912794, "Category": "false retweets"}, {"Dates": "2020-05-20T00:00:00", "Retweets": 0.001110544851559707, "Category": "partially false retweets"}, {"Dates": "2020-05-22T00:00:00", "Retweets": 0.0006617630279842089, "Category": "false retweets"}, {"Dates": "2020-05-25T00:00:00", "Retweets": 0.00022819414758076172, "Category": "partially false retweets"}, {"Dates": "2020-05-28T00:00:00", "Retweets": 0.0006617630279842089, "Category": "false retweets"}, {"Dates": "2020-05-29T00:00:00", "Retweets": 0.18605429499418105, "Category": "false retweets"}, {"Dates": "2020-05-01T00:00:00", "Retweets": 0.005628788973658789, "Category": "false retweets"}, {"Dates": "2020-05-02T00:00:00", "Retweets": 0.3198901625502978, "Category": "false retweets"}, {"Dates": "2020-05-04T00:00:00", "Retweets": 0.009705857743768398, "Category": "false retweets"}, {"Dates": "2020-05-08T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-05-08T00:00:00", "Retweets": 0.0007074018575003613, "Category": "partially false retweets"}, {"Dates": "2020-05-09T00:00:00", "Retweets": 0.0016049655046513575, "Category": "false retweets"}, {"Dates": "2020-05-11T00:00:00", "Retweets": 0.48438771706968287, "Category": "partially false retweets"}, {"Dates": "2020-05-12T00:00:00", "Retweets": 0.4920550404283965, "Category": "partially false retweets"}, {"Dates": "2020-05-15T00:00:00", "Retweets": 0.006031931967718135, "Category": "partially false retweets"}, {"Dates": "2020-05-17T00:00:00", "Retweets": 0.017198232256003407, "Category": "false retweets"}, {"Dates": "2020-05-21T00:00:00", "Retweets": 0.005278891280701621, "Category": "partially false retweets"}, {"Dates": "2020-05-05T00:00:00", "Retweets": 0.018141434732670558, "Category": "false retweets"}, {"Dates": "2020-05-15T00:00:00", "Retweets": 1.5212943172050781e-05, "Category": "false retweets"}, {"Dates": "2020-05-23T00:00:00", "Retweets": 3.0425886344101563e-05, "Category": "partially false retweets"}, {"Dates": "2020-05-04T00:00:00", "Retweets": 0.00011409707379038086, "Category": "partially false retweets"}, {"Dates": "2020-05-07T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-05-22T00:00:00", "Retweets": 7.606471586025391e-06, "Category": "partially false retweets"}, {"Dates": "2020-05-01T00:00:00", "Retweets": 0.0002586200339248633, "Category": "partially false retweets"}, {"Dates": "2020-05-13T00:00:00", "Retweets": 0.17214966493492664, "Category": "partially false retweets"}, {"Dates": "2020-05-14T00:00:00", "Retweets": 0.001110544851559707, "Category": "partially false retweets"}, {"Dates": "2020-05-30T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-05-30T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-5b9da91f45374622a0adce8eaede7d6b"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-5b9da91f45374622a0adce8eaede7d6b") {
      outputDiv = document.getElementById("altair-viz-5b9da91f45374622a0adce8eaede7d6b");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-59eeda2f460ba0cded2d9da540771690"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#007890", "#923800"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-62030df6cbeefe094b6aa2c41539a308"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#00C000", "#FF007F"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-59eeda2f460ba0cded2d9da540771690": [{"Dates": "2020-06-01T00:00:00", "Likes": 0.00040603182838388054, "Category": "partially false likes"}, {"Dates": "2020-06-04T00:00:00", "Likes": 0.026380790183052682, "Category": "false likes"}, {"Dates": "2020-06-06T00:00:00", "Likes": 0.13137385380598446, "Category": "false likes"}, {"Dates": "2020-06-08T00:00:00", "Likes": 0.06787498731150536, "Category": "false likes"}, {"Dates": "2020-06-08T00:00:00", "Likes": 0.01819248164397776, "Category": "partially false likes"}, {"Dates": "2020-06-09T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-06-10T00:00:00", "Likes": 3.3835985698656714e-05, "Category": "false likes"}, {"Dates": "2020-06-11T00:00:00", "Likes": 0.00016917992849328355, "Category": "false likes"}, {"Dates": "2020-06-11T00:00:00", "Likes": 0.0021993390704126863, "Category": "partially false likes"}, {"Dates": "2020-06-12T00:00:00", "Likes": 0.21810676381354116, "Category": "false likes"}, {"Dates": "2020-06-13T00:00:00", "Likes": 0.03557289963118775, "Category": "partially false likes"}, {"Dates": "2020-06-14T00:00:00", "Likes": 0.004894939264405671, "Category": "false likes"}, {"Dates": "2020-06-14T00:00:00", "Likes": 0.0025940922368970147, "Category": "partially false likes"}, {"Dates": "2020-06-16T00:00:00", "Likes": 0.5341687062246935, "Category": "false likes"}, {"Dates": "2020-06-17T00:00:00", "Likes": 0.19171469496858892, "Category": "false likes"}, {"Dates": "2020-06-24T00:00:00", "Likes": 0.02490328547421134, "Category": "false likes"}, {"Dates": "2020-06-24T00:00:00", "Likes": 0.0005188184473794029, "Category": "partially false likes"}, {"Dates": "2020-06-25T00:00:00", "Likes": 0.004319727507528507, "Category": "partially false likes"}, {"Dates": "2020-06-25T00:00:00", "Likes": 0.08172518412415551, "Category": "false likes"}, {"Dates": "2020-06-26T00:00:00", "Likes": 1.1278661899552237e-05, "Category": "partially false likes"}, {"Dates": "2020-06-01T00:00:00", "Likes": 0.003270811950870149, "Category": "false likes"}, {"Dates": "2020-06-02T00:00:00", "Likes": 0.0044776287741222385, "Category": "false likes"}, {"Dates": "2020-06-02T00:00:00", "Likes": 0.00020301591419194027, "Category": "partially false likes"}, {"Dates": "2020-06-04T00:00:00", "Likes": 0.00024813056179014923, "Category": "partially false likes"}, {"Dates": "2020-06-05T00:00:00", "Likes": 0.002932452093883582, "Category": "false likes"}, {"Dates": "2020-06-09T00:00:00", "Likes": 0.009406404024226565, "Category": "partially false likes"}, {"Dates": "2020-06-23T00:00:00", "Likes": 0.0017707499182297013, "Category": "false likes"}, {"Dates": "2020-06-03T00:00:00", "Likes": 0.00428589152182985, "Category": "false likes"}, {"Dates": "2020-06-03T00:00:00", "Likes": 0.001421111399343582, "Category": "partially false likes"}, {"Dates": "2020-06-18T00:00:00", "Likes": 0.06332968656598581, "Category": "partially false likes"}, {"Dates": "2020-06-28T00:00:00", "Likes": 0.011064367323460745, "Category": "false likes"}, {"Dates": "2020-06-05T00:00:00", "Likes": 0.0013083247803480594, "Category": "partially false likes"}, {"Dates": "2020-06-12T00:00:00", "Likes": 0.0023008470275086563, "Category": "partially false likes"}, {"Dates": "2020-06-27T00:00:00", "Likes": 0.00020301591419194027, "Category": "partially false likes"}, {"Dates": "2020-06-06T00:00:00", "Likes": 0.0005526544330780596, "Category": "partially false likes"}, {"Dates": "2020-06-13T00:00:00", "Likes": 0.0001466226046941791, "Category": "false likes"}, {"Dates": "2020-06-19T00:00:00", "Likes": 2.2557323799104474e-05, "Category": "partially false likes"}, {"Dates": "2020-06-18T00:00:00", "Likes": 0.0009135716138637312, "Category": "false likes"}, {"Dates": "2020-06-19T00:00:00", "Likes": 0.5134046896676179, "Category": "false likes"}, {"Dates": "2020-06-27T00:00:00", "Likes": 0.000902292951964179, "Category": "false likes"}, {"Dates": "2020-06-07T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-07T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-06-15T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-15T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-06-20T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-20T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-06-21T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-21T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-06-22T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-22T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-06-29T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-06-29T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-62030df6cbeefe094b6aa2c41539a308": [{"Dates": "2020-06-01T00:00:00", "Retweets": 0.0013762832911769082, "Category": "partially false retweets"}, {"Dates": "2020-06-04T00:00:00", "Retweets": 0.027079303675048357, "Category": "false retweets"}, {"Dates": "2020-06-06T00:00:00", "Retweets": 0.10775926201458116, "Category": "false retweets"}, {"Dates": "2020-06-08T00:00:00", "Retweets": 0.11616574914447254, "Category": "false retweets"}, {"Dates": "2020-06-08T00:00:00", "Retweets": 0.025479839309626544, "Category": "partially false retweets"}, {"Dates": "2020-06-09T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-06-10T00:00:00", "Retweets": 3.7196845707484004e-05, "Category": "false retweets"}, {"Dates": "2020-06-11T00:00:00", "Retweets": 0.0005951495313197441, "Category": "false retweets"}, {"Dates": "2020-06-11T00:00:00", "Retweets": 0.0047611962505579525, "Category": "partially false retweets"}, {"Dates": "2020-06-12T00:00:00", "Retweets": 0.12959381044487428, "Category": "false retweets"}, {"Dates": "2020-06-13T00:00:00", "Retweets": 0.017073352179735157, "Category": "partially false retweets"}, {"Dates": "2020-06-14T00:00:00", "Retweets": 0.004203243564945692, "Category": "false retweets"}, {"Dates": "2020-06-14T00:00:00", "Retweets": 0.007216188067251897, "Category": "partially false retweets"}, {"Dates": "2020-06-16T00:00:00", "Retweets": 0.44241928284481474, "Category": "false retweets"}, {"Dates": "2020-06-17T00:00:00", "Retweets": 0.02793483112632049, "Category": "false retweets"}, {"Dates": "2020-06-24T00:00:00", "Retweets": 0.010526707335217973, "Category": "false retweets"}, {"Dates": "2020-06-24T00:00:00", "Retweets": 0.0009299211426871001, "Category": "partially false retweets"}, {"Dates": "2020-06-25T00:00:00", "Retweets": 0.0026781728909388482, "Category": "partially false retweets"}, {"Dates": "2020-06-25T00:00:00", "Retweets": 0.0304642166344294, "Category": "false retweets"}, {"Dates": "2020-06-26T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-01T00:00:00", "Retweets": 0.007699747061449189, "Category": "false retweets"}, {"Dates": "2020-06-02T00:00:00", "Retweets": 0.005244755244755245, "Category": "false retweets"}, {"Dates": "2020-06-02T00:00:00", "Retweets": 0.00026037791995238803, "Category": "partially false retweets"}, {"Dates": "2020-06-04T00:00:00", "Retweets": 0.0004091653027823241, "Category": "partially false retweets"}, {"Dates": "2020-06-05T00:00:00", "Retweets": 0.0039056687992858204, "Category": "false retweets"}, {"Dates": "2020-06-09T00:00:00", "Retweets": 0.013948817140306501, "Category": "partially false retweets"}, {"Dates": "2020-06-23T00:00:00", "Retweets": 0.005058771016217825, "Category": "false retweets"}, {"Dates": "2020-06-03T00:00:00", "Retweets": 0.009671179883945842, "Category": "false retweets"}, {"Dates": "2020-06-03T00:00:00", "Retweets": 0.004054456182115756, "Category": "partially false retweets"}, {"Dates": "2020-06-18T00:00:00", "Retweets": 0.07800178544859396, "Category": "partially false retweets"}, {"Dates": "2020-06-28T00:00:00", "Retweets": 0.013130486534741853, "Category": "false retweets"}, {"Dates": "2020-06-05T00:00:00", "Retweets": 0.00022318107424490404, "Category": "partially false retweets"}, {"Dates": "2020-06-12T00:00:00", "Retweets": 0.0017110549025442642, "Category": "partially false retweets"}, {"Dates": "2020-06-27T00:00:00", "Retweets": 0.0004091653027823241, "Category": "partially false retweets"}, {"Dates": "2020-06-06T00:00:00", "Retweets": 0.0004091653027823241, "Category": "partially false retweets"}, {"Dates": "2020-06-13T00:00:00", "Retweets": 0.00011159053712245202, "Category": "false retweets"}, {"Dates": "2020-06-19T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-18T00:00:00", "Retweets": 0.0010787085255170362, "Category": "false retweets"}, {"Dates": "2020-06-19T00:00:00", "Retweets": 0.4440187472102366, "Category": "false retweets"}, {"Dates": "2020-06-27T00:00:00", "Retweets": 0.0015622675197143282, "Category": "false retweets"}, {"Dates": "2020-06-07T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-07T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-15T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-15T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-20T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-20T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-21T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-21T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-22T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-22T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-06-29T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-06-29T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-20439203325d46168e32964998ce7fb7"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-20439203325d46168e32964998ce7fb7") {
      outputDiv = document.getElementById("altair-viz-20439203325d46168e32964998ce7fb7");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-7730b4c7d6a75306c6d15065f002418f"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#0030FF", "#E66C2C"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-6067e7a77c3b13f830d992c25296085e"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#00FF7F", "#DE5D83"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-7730b4c7d6a75306c6d15065f002418f": [{"Dates": "2020-07-01T00:00:00", "Likes": 0.0003038610612178751, "Category": "partially false likes"}, {"Dates": "2020-07-03T00:00:00", "Likes": 0.010743176631058652, "Category": "false likes"}, {"Dates": "2020-07-08T00:00:00", "Likes": 0.006083973692384567, "Category": "partially false likes"}, {"Dates": "2020-07-18T00:00:00", "Likes": 0.007873377719556499, "Category": "partially false likes"}, {"Dates": "2020-07-24T00:00:00", "Likes": 0.06711953218901509, "Category": "false likes"}, {"Dates": "2020-07-30T00:00:00", "Likes": 0.0008575634394371143, "Category": "false likes"}, {"Dates": "2020-07-06T00:00:00", "Likes": 0.0008845733115453698, "Category": "false likes"}, {"Dates": "2020-07-27T00:00:00", "Likes": 0.01778600078328629, "Category": "false likes"}, {"Dates": "2020-07-21T00:00:00", "Likes": 0.028664226774886222, "Category": "false likes"}, {"Dates": "2020-07-28T00:00:00", "Likes": 0.027232703553148677, "Category": "false likes"}, {"Dates": "2020-07-30T00:00:00", "Likes": 0.003288451929180115, "Category": "partially false likes"}, {"Dates": "2020-07-02T00:00:00", "Likes": 0.0014045133496292895, "Category": "partially false likes"}, {"Dates": "2020-07-11T00:00:00", "Likes": 4.726727618944724e-05, "Category": "false likes"}, {"Dates": "2020-07-15T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-07-22T00:00:00", "Likes": 0.011553472794306319, "Category": "false likes"}, {"Dates": "2020-07-25T00:00:00", "Likes": 6.752468027063892e-06, "Category": "false likes"}, {"Dates": "2020-07-23T00:00:00", "Likes": 0.0048685294475130664, "Category": "false likes"}, {"Dates": "2020-07-14T00:00:00", "Likes": 0.00019582157278485285, "Category": "false likes"}, {"Dates": "2020-07-17T00:00:00", "Likes": 0.13753426877523736, "Category": "false likes"}, {"Dates": "2020-07-10T00:00:00", "Likes": 0.014240955069077748, "Category": "false likes"}, {"Dates": "2020-07-12T00:00:00", "Likes": 0.0053817170175699215, "Category": "partially false likes"}, {"Dates": "2020-07-13T00:00:00", "Likes": 0.0012154442448715004, "Category": "false likes"}, {"Dates": "2020-07-01T00:00:00", "Likes": 0.009527732386187152, "Category": "false likes"}, {"Dates": "2020-07-04T00:00:00", "Likes": 0.000499682634002728, "Category": "false likes"}, {"Dates": "2020-07-05T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-05T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-07T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-07T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-09T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-09T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-16T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-16T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-19T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-19T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-20T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-20T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-26T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-26T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-07-29T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-07-29T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-6067e7a77c3b13f830d992c25296085e": [{"Dates": "2020-07-01T00:00:00", "Retweets": 0.0006048652202498356, "Category": "partially false retweets"}, {"Dates": "2020-07-03T00:00:00", "Retweets": 0.013175542406311637, "Category": "false retweets"}, {"Dates": "2020-07-08T00:00:00", "Retweets": 0.0036028928336620646, "Category": "partially false retweets"}, {"Dates": "2020-07-18T00:00:00", "Retweets": 0.009441157133464826, "Category": "partially false retweets"}, {"Dates": "2020-07-24T00:00:00", "Retweets": 0.023431952662721894, "Category": "false retweets"}, {"Dates": "2020-07-30T00:00:00", "Retweets": 0.0015779092702169625, "Category": "false retweets"}, {"Dates": "2020-07-06T00:00:00", "Retweets": 0.0020512820512820513, "Category": "false retweets"}, {"Dates": "2020-07-27T00:00:00", "Retweets": 0.0012886259040105195, "Category": "false retweets"}, {"Dates": "2020-07-21T00:00:00", "Retweets": 0.032136752136752135, "Category": "false retweets"}, {"Dates": "2020-07-28T00:00:00", "Retweets": 0.026351084812623275, "Category": "false retweets"}, {"Dates": "2020-07-30T00:00:00", "Retweets": 0.003865877712031558, "Category": "partially false retweets"}, {"Dates": "2020-07-02T00:00:00", "Retweets": 0.0041025641025641026, "Category": "partially false retweets"}, {"Dates": "2020-07-11T00:00:00", "Retweets": 5.259697567389875e-05, "Category": "false retweets"}, {"Dates": "2020-07-15T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-07-22T00:00:00", "Retweets": 0.01388560157790927, "Category": "false retweets"}, {"Dates": "2020-07-25T00:00:00", "Retweets": 2.6298487836949376e-05, "Category": "false retweets"}, {"Dates": "2020-07-23T00:00:00", "Retweets": 0.0016042077580539118, "Category": "false retweets"}, {"Dates": "2020-07-14T00:00:00", "Retweets": 0.0007626561472715319, "Category": "false retweets"}, {"Dates": "2020-07-17T00:00:00", "Retweets": 0.13664694280078896, "Category": "false retweets"}, {"Dates": "2020-07-10T00:00:00", "Retweets": 0.007626561472715319, "Category": "false retweets"}, {"Dates": "2020-07-12T00:00:00", "Retweets": 0.005943458251150559, "Category": "partially false retweets"}, {"Dates": "2020-07-13T00:00:00", "Retweets": 0.0016305062458908614, "Category": "false retweets"}, {"Dates": "2020-07-01T00:00:00", "Retweets": 0.019250493096646944, "Category": "false retweets"}, {"Dates": "2020-07-04T00:00:00", "Retweets": 0.0013149243918474688, "Category": "false retweets"}, {"Dates": "2020-07-05T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-05T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-07T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-07T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-09T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-09T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-16T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-16T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-19T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-19T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-20T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-20T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-26T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-26T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-07-29T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-07-29T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-f1f443fd68ce489db303bb48741a05cf"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-f1f443fd68ce489db303bb48741a05cf") {
      outputDiv = document.getElementById("altair-viz-f1f443fd68ce489db303bb48741a05cf");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.8.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-1b9f15aa13e1b0d28acf2b6bfde01d8d"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#0087FF", "#FF862E"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 110, "width": 250}, {"data": {"name": "data-922ffb7362d9024e797552163b891ac7"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Category", "scale": {"range": ["#008000", "#F791F5"]}}, "row": {"type": "nominal", "field": "Category"}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 110, "width": 250}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-1b9f15aa13e1b0d28acf2b6bfde01d8d": [{"Dates": "2020-08-07T00:00:00", "Likes": 0.0043418013856812935, "Category": "partially false likes"}, {"Dates": "2020-08-11T00:00:00", "Likes": 0.08468052347959969, "Category": "partially false likes"}, {"Dates": "2020-08-12T00:00:00", "Likes": 0.0068668206312548115, "Category": "partially false likes"}, {"Dates": "2020-08-13T00:00:00", "Likes": 0.03458044649730562, "Category": "partially false likes"}, {"Dates": "2020-08-06T00:00:00", "Likes": 0.04612779060816012, "Category": "partially false likes"}, {"Dates": "2020-08-07T00:00:00", "Likes": 0.11996920708237105, "Category": "false likes"}, {"Dates": "2020-08-08T00:00:00", "Likes": 0.11313317936874519, "Category": "false likes"}, {"Dates": "2020-08-11T00:00:00", "Likes": 0.0002771362586605081, "Category": "false likes"}, {"Dates": "2020-08-12T00:00:00", "Likes": 0.26346420323325637, "Category": "false likes"}, {"Dates": "2020-08-15T00:00:00", "Likes": 6.158583525789069e-05, "Category": "false likes"}, {"Dates": "2020-08-09T00:00:00", "Likes": 0.0004926866820631255, "Category": "partially false likes"}, {"Dates": "2020-08-10T00:00:00", "Likes": 0.048652809853733645, "Category": "false likes"}, {"Dates": "2020-08-26T00:00:00", "Likes": 1.0, "Category": "false likes"}, {"Dates": "2020-08-01T00:00:00", "Likes": 0.15990762124711316, "Category": "false likes"}, {"Dates": "2020-08-02T00:00:00", "Likes": 0.24742109314857583, "Category": "false likes"}, {"Dates": "2020-08-03T00:00:00", "Likes": 0.01527328714395689, "Category": "partially false likes"}, {"Dates": "2020-08-04T00:00:00", "Likes": 0.0002155504234026174, "Category": "false likes"}, {"Dates": "2020-08-27T00:00:00", "Likes": 0.27125481139337954, "Category": "partially false likes"}, {"Dates": "2020-08-30T00:00:00", "Likes": 0.0011393379522709776, "Category": "false likes"}, {"Dates": "2020-08-18T00:00:00", "Likes": 0.024449576597382602, "Category": "partially false likes"}, {"Dates": "2020-08-18T00:00:00", "Likes": 0.009792147806004618, "Category": "false likes"}, {"Dates": "2020-08-20T00:00:00", "Likes": 0.0024018475750577366, "Category": "false likes"}, {"Dates": "2020-08-16T00:00:00", "Likes": 0.016782140107775213, "Category": "false likes"}, {"Dates": "2020-08-19T00:00:00", "Likes": 0.05665896843725943, "Category": "false likes"}, {"Dates": "2020-08-05T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-05T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-14T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-14T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-17T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-17T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-21T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-21T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-22T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-22T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-23T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-23T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-24T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-24T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-25T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-25T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-28T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-28T00:00:00", "Likes": 0.0, "Category": "partially false likes"}, {"Dates": "2020-08-29T00:00:00", "Likes": 0.0, "Category": "false likes"}, {"Dates": "2020-08-29T00:00:00", "Likes": 0.0, "Category": "partially false likes"}], "data-922ffb7362d9024e797552163b891ac7": [{"Dates": "2020-08-07T00:00:00", "Retweets": 0.013128402177393531, "Category": "partially false retweets"}, {"Dates": "2020-08-11T00:00:00", "Retweets": 0.3291706692283061, "Category": "partially false retweets"}, {"Dates": "2020-08-12T00:00:00", "Retweets": 0.05731668267691323, "Category": "partially false retweets"}, {"Dates": "2020-08-13T00:00:00", "Retweets": 0.06532180595581172, "Category": "partially false retweets"}, {"Dates": "2020-08-06T00:00:00", "Retweets": 0.24815882164585334, "Category": "partially false retweets"}, {"Dates": "2020-08-07T00:00:00", "Retweets": 0.8149215497918668, "Category": "false retweets"}, {"Dates": "2020-08-08T00:00:00", "Retweets": 0.14185078450208133, "Category": "false retweets"}, {"Dates": "2020-08-11T00:00:00", "Retweets": 0.001280819724623759, "Category": "false retweets"}, {"Dates": "2020-08-12T00:00:00", "Retweets": 0.8290105667627281, "Category": "false retweets"}, {"Dates": "2020-08-15T00:00:00", "Retweets": 0.0003202049311559398, "Category": "false retweets"}, {"Dates": "2020-08-09T00:00:00", "Retweets": 0.002241434518091579, "Category": "partially false retweets"}, {"Dates": "2020-08-10T00:00:00", "Retweets": 0.11655459494076209, "Category": "false retweets"}, {"Dates": "2020-08-26T00:00:00", "Retweets": 1.0, "Category": "false retweets"}, {"Dates": "2020-08-01T00:00:00", "Retweets": 0.7729747038104386, "Category": "false retweets"}, {"Dates": "2020-08-02T00:00:00", "Retweets": 0.22382324687800192, "Category": "false retweets"}, {"Dates": "2020-08-03T00:00:00", "Retweets": 0.09990393852065321, "Category": "partially false retweets"}, {"Dates": "2020-08-04T00:00:00", "Retweets": 0.001601024655779699, "Category": "false retweets"}, {"Dates": "2020-08-27T00:00:00", "Retweets": 0.8229266730707653, "Category": "partially false retweets"}, {"Dates": "2020-08-30T00:00:00", "Retweets": 0.007684918347742555, "Category": "false retweets"}, {"Dates": "2020-08-18T00:00:00", "Retweets": 0.027857829010566763, "Category": "partially false retweets"}, {"Dates": "2020-08-18T00:00:00", "Retweets": 0.044508485430675634, "Category": "false retweets"}, {"Dates": "2020-08-20T00:00:00", "Retweets": 0.018892090938200448, "Category": "false retweets"}, {"Dates": "2020-08-16T00:00:00", "Retweets": 0.01536983669548511, "Category": "false retweets"}, {"Dates": "2020-08-19T00:00:00", "Retweets": 0.2811399295549151, "Category": "false retweets"}, {"Dates": "2020-08-05T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-05T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-14T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-14T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-17T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-17T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-21T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-21T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-22T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-22T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-23T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-23T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-24T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-24T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-25T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-25T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-28T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-28T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}, {"Dates": "2020-08-29T00:00:00", "Retweets": 0.0, "Category": "false retweets"}, {"Dates": "2020-08-29T00:00:00", "Retweets": 0.0, "Category": "partially false retweets"}]}}, {"mode": "vega-lite"});
</script>



# Recap

## January 2020

![january_fake.png](attachment:january_fake.png)

## February 2020

![february_fake.png](attachment:february_fake.png)

## March 2020

![march_fake.png](attachment:march_fake.png)

## April 2020

![april_fake.png](attachment:april_fake.png)

## May 2020

![may_fake.png](attachment:may_fake.png)

## June 2020

![june_fake.png](attachment:june_fake.png)

## July 2020

![july_fake.png](attachment:july_fake.png)

## August

![august_fake.png](attachment:august_fake.png)
