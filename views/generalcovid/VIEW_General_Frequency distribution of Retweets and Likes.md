# Frequency distribution of Retweets and Likes for each month until July 2020

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

alt.data_transformers.disable_max_rows()
```

To read the JSON file that has all the tweets, it is necessary to do:


```python
data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
```

## January 2020

We're interested in the "retweet_count" and "favorite_count" fields:


```python
start = utc.localize(datetime.datetime(2020, 1, 1))
end = utc.localize(datetime.datetime(2020, 1, 31))

index=0
dates = ["2020-01-14"] 
retweets = [0]
likes = [0]

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1



# Fill the empty dates with 0.
start = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-01-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)
```

We create the DataFrames which will be used to realize the chart, one for the Retweets count and one for the Likes count:


```python
mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates)

df_likes_jan = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_jan['Dates']= pd.to_datetime(df_likes_jan['Dates'])



df_retweets_jan = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_jan['Dates']= pd.to_datetime(df_retweets_jan['Dates'])



df_jan = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#A8D8A8']))
).properties(
    width=280,
    height=130
)
c1_jan.encoding.x.title = 'Dates'
c1_jan.encoding.y.title = 'Norm. Count'

c2_jan = alt.Chart(df_retweets_jan).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#F3C0E0']))
).properties(
    width=280,
    height=130
)
c2_jan.encoding.x.title = 'Dates'
c2_jan.encoding.y.title = 'Norm. Count'
```

We normalised the count of Retweets and Likes for the overall month together and plotted the normalised count of Retweets and Likes for each month, until July 2020.

## February 2020


```python
start = utc.localize(datetime.datetime(2020, 2, 1))
end = utc.localize(datetime.datetime(2020, 2, 29))

index=0
dates = ["2020-02-01"] 
retweets = [0]
likes = [0]

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-02-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-02-29", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

        
mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates)

df_likes_feb = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type': mipiace
    })

df_likes_feb['Dates']= pd.to_datetime(df_likes_feb['Dates'])



df_retweets_feb = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_feb['Dates']= pd.to_datetime(df_retweets_feb['Dates'])



df_feb = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#009E73']))
).properties(
    width=280,
    height=130
)
c1_feb.encoding.x.title = 'Dates'
c1_feb.encoding.y.title = 'Norm. Count'

c2_feb = alt.Chart(df_retweets_feb).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#FF4C9D']))
).properties(
    width=280,
    height=130
)
c2_feb.encoding.x.title = 'Dates'
c2_feb.encoding.y.title = 'Norm. Count'
```

## March 2020


```python
start = utc.localize(datetime.datetime(2020, 3, 1))
end = utc.localize(datetime.datetime(2020, 3, 31))

index=0
dates = ["2020-03-01"] 
retweets = [0]
likes = [0]

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-03-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

        
mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates)

df_likes_mar = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_mar['Dates']= pd.to_datetime(df_likes_mar['Dates'])



df_retweets_mar = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_mar['Dates']= pd.to_datetime(df_retweets_mar['Dates'])



df_mar = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#024429']))
).properties(
    width=280,
    height=130
)
c1_mar.encoding.x.title = 'Dates'
c1_mar.encoding.y.title = 'Norm. Count'

c2_mar = alt.Chart(df_retweets_mar).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#DC7AC3']))
).properties(
    width=280,
    height=130
)
c2_mar.encoding.x.title = 'Dates'
c2_mar.encoding.y.title = 'Norm. Count'
```

## April 2020


```python
start = utc.localize(datetime.datetime(2020, 4, 1))
end = utc.localize(datetime.datetime(2020, 4, 30))

index=0
dates = ["2020-04-01"] 
retweets = [0]
likes = [0]

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-04-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-04-30", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates)        

df_likes_apr = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_apr['Dates']= pd.to_datetime(df_likes_apr['Dates'])



df_retweets_apr = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_apr['Dates']= pd.to_datetime(df_retweets_apr['Dates'])



df_apr = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#609048']))
).properties(
    width=280,
    height=130
)
c1_apr.encoding.x.title = 'Dates'
c1_apr.encoding.y.title = 'Norm. Count'

c2_apr = alt.Chart(df_retweets_apr).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#AA4499']))
).properties(
    width=280,
    height=130
)
c2_apr.encoding.x.title = 'Dates'
c2_apr.encoding.y.title = 'Norm. Count'
```

## May 2020


```python
start = utc.localize(datetime.datetime(2020, 5, 1))
end = utc.localize(datetime.datetime(2020, 5, 31))

index=0
dates = ["2020-05-01"] 
retweets = [0]
likes = [0]

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-05-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-05-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates)                

df_likes_may = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_may['Dates']= pd.to_datetime(df_likes_may['Dates'])



df_retweets_may = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_may['Dates']= pd.to_datetime(df_retweets_may['Dates'])



df_may = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#117733']))
).properties(
    width=280,
    height=130
)
c1_may.encoding.x.title = 'Dates'
c1_may.encoding.y.title = 'Norm. Count'

c2_may = alt.Chart(df_retweets_may).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#9A1557']))
).properties(
    width=280,
    height=130
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

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-06-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-06-30", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

        
mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates) 

df_likes_jun = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_jun['Dates']= pd.to_datetime(df_likes_jun['Dates'])



df_retweets_jun = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_jun['Dates']= pd.to_datetime(df_retweets_jun['Dates'])



df_jun = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#00C000']))
).properties(
    width=280,
    height=130
)
c1_jun.encoding.x.title = 'Dates'
c1_jun.encoding.y.title = 'Norm. Count'

c2_jun = alt.Chart(df_retweets_jun).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#D2458B']))
).properties(
    width=280,
    height=130
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

for element in data:
    token = data[index]['created_at']
    d = parse(token)
   
    if start <= d <= end:
        d = d.strftime('%Y-%m-%d')
        if d in dates:
            i = dates.index(d)
            retweets[i] = retweets[i] + data[index]['retweet_count']
            likes[i] = likes[i]+ data[index]['favorite_count']
        else:
            dates.append(d)
            retweets.append(data[index]['retweet_count'])
            likes.append(data[index]['favorite_count'])
        
       
    index=index+1

    

start = datetime.datetime.strptime("2020-07-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-07-31", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    if date.strftime("%Y-%m-%d") not in dates:
        d = date.strftime("%Y-%m-%d")
        dates.append(d)
        retweets.append(0)
        likes.append(0)

        
mipiace = ['Likes'] * len(dates)
rts = ['Retweets'] * len(dates) 

df_likes_jul = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Type':mipiace
    })

df_likes_jul['Dates']= pd.to_datetime(df_likes_jul['Dates'])



df_retweets_jul = pd.DataFrame(
    {'Dates': dates,
     'Retweets': retweets,
     'Type':rts
    })

df_retweets_jul['Dates']= pd.to_datetime(df_retweets_jul['Dates'])



df_jul = pd.DataFrame(
    {'Dates': dates,
     'Likes': likes,
     'Retweets': retweets
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
    color=alt.Color('Type:N',scale=alt.Scale(range=['#00FF7F']))
).properties(
    width=280,
    height=130
)
c1_jul.encoding.x.title = 'Dates'
c1_jul.encoding.y.title = 'Norm. Count'

c2_jul = alt.Chart(df_retweets_jul).mark_line().encode(
    x="monthdate(Dates):T",
    y="Retweets",
    color=alt.Color('Type:N',scale=alt.Scale(range=['#FF83A8']))
).properties(
    width=280,
    height=130
)
c2_jul.encoding.x.title = 'Dates'
c2_jul.encoding.y.title = 'Norm. Count'
```

To summarize you can find below every chart produced in this notebook.

## January 2020


```python
alt.hconcat(c1_jan, c2_jan).configure_axis(
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
).resolve_scale(
    color='independent'
)
```


## February 2020


```python
alt.hconcat(c1_feb, c2_feb).configure_axis(
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
).resolve_scale(
    color='independent'
)
```

## March 2020


```python
alt.hconcat(c1_mar, c2_mar).configure_axis(
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
).resolve_scale(
    color='independent'
)
```

## April 2020


```python
alt.hconcat(c1_apr, c2_apr).configure_axis(
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
).resolve_scale(
    color='independent'
)
```

## May 2020


```python
alt.hconcat(c1_may, c2_may).configure_axis(
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
).resolve_scale(
    color='independent'
)
```

## June 2020


```python
alt.hconcat(c1_jun, c2_jun).configure_axis(
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
).resolve_scale(
    color='independent'
)
```

## July 2020


```python
alt.hconcat(c1_jul, c2_jul).configure_axis(
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
).resolve_scale(
    color='independent'
)
```


# Recap

## January 2020

![1_jan2020.png](./img/1_jan2020.png)

## February 2020

![2_feb2020.png](./img/2_feb2020.png)

## March 2020

![3_mar2020.png](./img/3_mar2020.png)

## April 2020

![4_apr2020.png](./img/4_apr2020.png)

## May 2020

![5_may2020.png](./img/5_may2020.png)

## June 2020

![6_june2020.png](./img/6_june2020.png)

## July 2020

![7_jul2020.png](./img/7_jul2020.png)
