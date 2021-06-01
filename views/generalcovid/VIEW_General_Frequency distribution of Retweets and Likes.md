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




    DataTransformerRegistry.enable('default')



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





<div id="altair-viz-a6c58a0034cf4ca4a9efc4976fe417e2"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-a6c58a0034cf4ca4a9efc4976fe417e2") {
      outputDiv = document.getElementById("altair-viz-a6c58a0034cf4ca4a9efc4976fe417e2");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-f23720f4bd09764ed9be5e1cb8292ebe"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#A8D8A8"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-94eebd0c41b33eaf985bab87489c6ce9"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#F3C0E0"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-f23720f4bd09764ed9be5e1cb8292ebe": [{"Dates": "2020-01-14T00:00:00", "Likes": 0.6095387274494977, "Type": "Likes"}, {"Dates": "2020-01-15T00:00:00", "Likes": 0.5306679115418448, "Type": "Likes"}, {"Dates": "2020-01-16T00:00:00", "Likes": 0.3673667803515486, "Type": "Likes"}, {"Dates": "2020-01-17T00:00:00", "Likes": 0.438151051713761, "Type": "Likes"}, {"Dates": "2020-01-18T00:00:00", "Likes": 0.2994220589823917, "Type": "Likes"}, {"Dates": "2020-01-19T00:00:00", "Likes": 0.45831339989814657, "Type": "Likes"}, {"Dates": "2020-01-20T00:00:00", "Likes": 0.8152749270822081, "Type": "Likes"}, {"Dates": "2020-01-21T00:00:00", "Likes": 0.2352312535687279, "Type": "Likes"}, {"Dates": "2020-01-22T00:00:00", "Likes": 0.5269680087655674, "Type": "Likes"}, {"Dates": "2020-01-23T00:00:00", "Likes": 0.4775073689408787, "Type": "Likes"}, {"Dates": "2020-01-24T00:00:00", "Likes": 0.3902336455809503, "Type": "Likes"}, {"Dates": "2020-01-25T00:00:00", "Likes": 0.41683513634469666, "Type": "Likes"}, {"Dates": "2020-01-26T00:00:00", "Likes": 0.18032299881171004, "Type": "Likes"}, {"Dates": "2020-01-27T00:00:00", "Likes": 0.19820521921634593, "Type": "Likes"}, {"Dates": "2020-01-28T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-01-29T00:00:00", "Likes": 0.6588489019892282, "Type": "Likes"}, {"Dates": "2020-01-30T00:00:00", "Likes": 0.4225528171731045, "Type": "Likes"}, {"Dates": "2020-01-01T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-02T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-03T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-04T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-05T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-06T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-07T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-08T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-09T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-10T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-11T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-12T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-01-13T00:00:00", "Likes": 0.0, "Type": "Likes"}], "data-94eebd0c41b33eaf985bab87489c6ce9": [{"Dates": "2020-01-14T00:00:00", "Retweets": 0.3566420309045622, "Type": "Retweets"}, {"Dates": "2020-01-15T00:00:00", "Retweets": 0.13547578909298785, "Type": "Retweets"}, {"Dates": "2020-01-16T00:00:00", "Retweets": 0.09830339903518033, "Type": "Retweets"}, {"Dates": "2020-01-17T00:00:00", "Retweets": 0.09210411185841534, "Type": "Retweets"}, {"Dates": "2020-01-18T00:00:00", "Retweets": 0.1199301759891735, "Type": "Retweets"}, {"Dates": "2020-01-19T00:00:00", "Retweets": 0.14898268107868473, "Type": "Retweets"}, {"Dates": "2020-01-20T00:00:00", "Retweets": 0.7193914752874334, "Type": "Retweets"}, {"Dates": "2020-01-21T00:00:00", "Retweets": 0.1167379295459981, "Type": "Retweets"}, {"Dates": "2020-01-22T00:00:00", "Retweets": 0.28958152259509656, "Type": "Retweets"}, {"Dates": "2020-01-23T00:00:00", "Retweets": 0.371179949950709, "Type": "Retweets"}, {"Dates": "2020-01-24T00:00:00", "Retweets": 0.2959470574166866, "Type": "Retweets"}, {"Dates": "2020-01-25T00:00:00", "Retweets": 0.302716544848948, "Type": "Retweets"}, {"Dates": "2020-01-26T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-01-27T00:00:00", "Retweets": 0.07517310171439238, "Type": "Retweets"}, {"Dates": "2020-01-28T00:00:00", "Retweets": 0.42387462010954846, "Type": "Retweets"}, {"Dates": "2020-01-29T00:00:00", "Retweets": 0.11355589129154003, "Type": "Retweets"}, {"Dates": "2020-01-30T00:00:00", "Retweets": 0.13856449533631607, "Type": "Retweets"}, {"Dates": "2020-01-01T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-02T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-03T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-04T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-05T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-06T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-07T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-08T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-09T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-10T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-11T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-12T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-01-13T00:00:00", "Retweets": 0.0, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-6cbef5467b984048bf0732edb0d46ec7"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-6cbef5467b984048bf0732edb0d46ec7") {
      outputDiv = document.getElementById("altair-viz-6cbef5467b984048bf0732edb0d46ec7");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-8bd3086308b9a53ca83572e23bbc5f51"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#009E73"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-4a0eeca18c555678d2f36d37f7ce65ee"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#FF4C9D"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-8bd3086308b9a53ca83572e23bbc5f51": [{"Dates": "2020-02-01T00:00:00", "Likes": 0.02916774984630936, "Type": "Likes"}, {"Dates": "2020-02-02T00:00:00", "Likes": 0.020910852734800804, "Type": "Likes"}, {"Dates": "2020-02-03T00:00:00", "Likes": 0.02365329623187371, "Type": "Likes"}, {"Dates": "2020-02-04T00:00:00", "Likes": 0.05499112443530545, "Type": "Likes"}, {"Dates": "2020-02-05T00:00:00", "Likes": 0.9236941316395193, "Type": "Likes"}, {"Dates": "2020-02-06T00:00:00", "Likes": 0.16218406950498784, "Type": "Likes"}, {"Dates": "2020-02-07T00:00:00", "Likes": 0.07407554104125827, "Type": "Likes"}, {"Dates": "2020-02-08T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-02-09T00:00:00", "Likes": 0.02216380800217789, "Type": "Likes"}, {"Dates": "2020-02-10T00:00:00", "Likes": 0.001985426445500909, "Type": "Likes"}, {"Dates": "2020-02-11T00:00:00", "Likes": 0.018422235883612394, "Type": "Likes"}, {"Dates": "2020-02-12T00:00:00", "Likes": 0.10197527337966553, "Type": "Likes"}, {"Dates": "2020-02-13T00:00:00", "Likes": 0.11822408374159443, "Type": "Likes"}, {"Dates": "2020-02-14T00:00:00", "Likes": 0.08385316658503304, "Type": "Likes"}, {"Dates": "2020-02-15T00:00:00", "Likes": 0.02945225883400407, "Type": "Likes"}, {"Dates": "2020-02-16T00:00:00", "Likes": 0.04542715956268179, "Type": "Likes"}, {"Dates": "2020-02-17T00:00:00", "Likes": 0.012235560053152973, "Type": "Likes"}, {"Dates": "2020-02-18T00:00:00", "Likes": 0.028291350592057625, "Type": "Likes"}, {"Dates": "2020-02-19T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-02-20T00:00:00", "Likes": 0.6547221239767439, "Type": "Likes"}, {"Dates": "2020-02-21T00:00:00", "Likes": 0.04757436562863655, "Type": "Likes"}, {"Dates": "2020-02-22T00:00:00", "Likes": 0.021111682608467658, "Type": "Likes"}, {"Dates": "2020-02-23T00:00:00", "Likes": 0.02241149817970034, "Type": "Likes"}, {"Dates": "2020-02-24T00:00:00", "Likes": 0.02669084807108485, "Type": "Likes"}, {"Dates": "2020-02-25T00:00:00", "Likes": 0.10144753710052985, "Type": "Likes"}, {"Dates": "2020-02-26T00:00:00", "Likes": 0.07487551337136455, "Type": "Likes"}, {"Dates": "2020-02-27T00:00:00", "Likes": 0.06432692425701314, "Type": "Likes"}, {"Dates": "2020-02-28T00:00:00", "Likes": 0.026307039868077087, "Type": "Likes"}], "data-4a0eeca18c555678d2f36d37f7ce65ee": [{"Dates": "2020-02-01T00:00:00", "Retweets": 0.21059828897308278, "Type": "Retweets"}, {"Dates": "2020-02-02T00:00:00", "Retweets": 0.11980674491310969, "Type": "Retweets"}, {"Dates": "2020-02-03T00:00:00", "Retweets": 0.04455515360103188, "Type": "Retweets"}, {"Dates": "2020-02-04T00:00:00", "Retweets": 0.14149485883790247, "Type": "Retweets"}, {"Dates": "2020-02-05T00:00:00", "Retweets": 0.7740534921713943, "Type": "Retweets"}, {"Dates": "2020-02-06T00:00:00", "Retweets": 0.34239236360351966, "Type": "Retweets"}, {"Dates": "2020-02-07T00:00:00", "Retweets": 0.08493494516569136, "Type": "Retweets"}, {"Dates": "2020-02-08T00:00:00", "Retweets": 0.16674193410375499, "Type": "Retweets"}, {"Dates": "2020-02-09T00:00:00", "Retweets": 0.8486443146147179, "Type": "Retweets"}, {"Dates": "2020-02-10T00:00:00", "Retweets": 0.047486622203418566, "Type": "Retweets"}, {"Dates": "2020-02-11T00:00:00", "Retweets": 0.6061468935147991, "Type": "Retweets"}, {"Dates": "2020-02-12T00:00:00", "Retweets": 0.4189116170139269, "Type": "Retweets"}, {"Dates": "2020-02-13T00:00:00", "Retweets": 0.20514892652788935, "Type": "Retweets"}, {"Dates": "2020-02-14T00:00:00", "Retweets": 0.1681506236105235, "Type": "Retweets"}, {"Dates": "2020-02-15T00:00:00", "Retweets": 0.08009564510531895, "Type": "Retweets"}, {"Dates": "2020-02-16T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-02-17T00:00:00", "Retweets": 0.17479317300576944, "Type": "Retweets"}, {"Dates": "2020-02-18T00:00:00", "Retweets": 0.15943861583975483, "Type": "Retweets"}, {"Dates": "2020-02-19T00:00:00", "Retweets": 0.8632620431860786, "Type": "Retweets"}, {"Dates": "2020-02-20T00:00:00", "Retweets": 0.4302413470177457, "Type": "Retweets"}, {"Dates": "2020-02-21T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-02-22T00:00:00", "Retweets": 0.4409927061892017, "Type": "Retweets"}, {"Dates": "2020-02-23T00:00:00", "Retweets": 0.3478940171102692, "Type": "Retweets"}, {"Dates": "2020-02-24T00:00:00", "Retweets": 0.5414073901531178, "Type": "Retweets"}, {"Dates": "2020-02-25T00:00:00", "Retweets": 0.08863018018232151, "Type": "Retweets"}, {"Dates": "2020-02-26T00:00:00", "Retweets": 0.11633968907417883, "Type": "Retweets"}, {"Dates": "2020-02-27T00:00:00", "Retweets": 0.281875759606898, "Type": "Retweets"}, {"Dates": "2020-02-28T00:00:00", "Retweets": 0.35469819342305214, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-2420173e6c1441e59283a90f9b76ee63"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-2420173e6c1441e59283a90f9b76ee63") {
      outputDiv = document.getElementById("altair-viz-2420173e6c1441e59283a90f9b76ee63");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-42c66152c626a26cc7511ad7839261e8"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#024429"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-89079dab0049ad1bce2d2b5ed7bc4740"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#DC7AC3"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-42c66152c626a26cc7511ad7839261e8": [{"Dates": "2020-03-01T00:00:00", "Likes": 0.28854435227084635, "Type": "Likes"}, {"Dates": "2020-03-02T00:00:00", "Likes": 0.6773122964317876, "Type": "Likes"}, {"Dates": "2020-03-03T00:00:00", "Likes": 0.01571034610453552, "Type": "Likes"}, {"Dates": "2020-03-04T00:00:00", "Likes": 0.09540247942926557, "Type": "Likes"}, {"Dates": "2020-03-05T00:00:00", "Likes": 0.00819182332593638, "Type": "Likes"}, {"Dates": "2020-03-06T00:00:00", "Likes": 0.02677491843244411, "Type": "Likes"}, {"Dates": "2020-03-07T00:00:00", "Likes": 0.10733532892134447, "Type": "Likes"}, {"Dates": "2020-03-08T00:00:00", "Likes": 0.07820666399216727, "Type": "Likes"}, {"Dates": "2020-03-09T00:00:00", "Likes": 0.2695909418633032, "Type": "Likes"}, {"Dates": "2020-03-10T00:00:00", "Likes": 0.23896558592577422, "Type": "Likes"}, {"Dates": "2020-03-11T00:00:00", "Likes": 0.0641402933907135, "Type": "Likes"}, {"Dates": "2020-03-12T00:00:00", "Likes": 0.35369459648256574, "Type": "Likes"}, {"Dates": "2020-03-13T00:00:00", "Likes": 0.1424142874376145, "Type": "Likes"}, {"Dates": "2020-03-14T00:00:00", "Likes": 0.1027891475173445, "Type": "Likes"}, {"Dates": "2020-03-15T00:00:00", "Likes": 0.06745068774845492, "Type": "Likes"}, {"Dates": "2020-03-16T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-03-17T00:00:00", "Likes": 0.2126198965922576, "Type": "Likes"}, {"Dates": "2020-03-18T00:00:00", "Likes": 0.11035536241804669, "Type": "Likes"}, {"Dates": "2020-03-19T00:00:00", "Likes": 0.49207188605510405, "Type": "Likes"}, {"Dates": "2020-03-20T00:00:00", "Likes": 0.06765688604107695, "Type": "Likes"}, {"Dates": "2020-03-21T00:00:00", "Likes": 0.08161945614148289, "Type": "Likes"}, {"Dates": "2020-03-22T00:00:00", "Likes": 0.183433720574662, "Type": "Likes"}, {"Dates": "2020-03-23T00:00:00", "Likes": 0.053802324570139684, "Type": "Likes"}, {"Dates": "2020-03-24T00:00:00", "Likes": 0.08982390385268184, "Type": "Likes"}, {"Dates": "2020-03-25T00:00:00", "Likes": 0.008275985894353534, "Type": "Likes"}, {"Dates": "2020-03-26T00:00:00", "Likes": 0.042012551444369946, "Type": "Likes"}, {"Dates": "2020-03-27T00:00:00", "Likes": 0.03270837950585351, "Type": "Likes"}, {"Dates": "2020-03-28T00:00:00", "Likes": 0.05784493327311034, "Type": "Likes"}, {"Dates": "2020-03-29T00:00:00", "Likes": 0.04179372876648534, "Type": "Likes"}, {"Dates": "2020-03-30T00:00:00", "Likes": 0.0, "Type": "Likes"}], "data-89079dab0049ad1bce2d2b5ed7bc4740": [{"Dates": "2020-03-01T00:00:00", "Retweets": 0.4799615938276202, "Type": "Retweets"}, {"Dates": "2020-03-02T00:00:00", "Retweets": 0.16367706286942044, "Type": "Retweets"}, {"Dates": "2020-03-03T00:00:00", "Retweets": 0.08399994863959118, "Type": "Retweets"}, {"Dates": "2020-03-04T00:00:00", "Retweets": 0.49277744250844235, "Type": "Retweets"}, {"Dates": "2020-03-05T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-03-06T00:00:00", "Retweets": 0.08643243466884663, "Type": "Retweets"}, {"Dates": "2020-03-07T00:00:00", "Retweets": 0.18977528394459353, "Type": "Retweets"}, {"Dates": "2020-03-08T00:00:00", "Retweets": 0.10708502573013814, "Type": "Retweets"}, {"Dates": "2020-03-09T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-03-10T00:00:00", "Retweets": 0.15257322781622676, "Type": "Retweets"}, {"Dates": "2020-03-11T00:00:00", "Retweets": 0.4384010363389159, "Type": "Retweets"}, {"Dates": "2020-03-12T00:00:00", "Retweets": 0.39881785459012253, "Type": "Retweets"}, {"Dates": "2020-03-13T00:00:00", "Retweets": 0.16762753431517316, "Type": "Retweets"}, {"Dates": "2020-03-14T00:00:00", "Retweets": 0.6451666288596991, "Type": "Retweets"}, {"Dates": "2020-03-15T00:00:00", "Retweets": 0.4076903652153071, "Type": "Retweets"}, {"Dates": "2020-03-16T00:00:00", "Retweets": 0.5652940597407156, "Type": "Retweets"}, {"Dates": "2020-03-17T00:00:00", "Retweets": 0.28437117026118197, "Type": "Retweets"}, {"Dates": "2020-03-18T00:00:00", "Retweets": 0.19916282533608967, "Type": "Retweets"}, {"Dates": "2020-03-19T00:00:00", "Retweets": 0.28629147888017187, "Type": "Retweets"}, {"Dates": "2020-03-20T00:00:00", "Retweets": 0.14296597800918495, "Type": "Retweets"}, {"Dates": "2020-03-21T00:00:00", "Retweets": 0.19572310462257947, "Type": "Retweets"}, {"Dates": "2020-03-22T00:00:00", "Retweets": 0.16815540518369193, "Type": "Retweets"}, {"Dates": "2020-03-23T00:00:00", "Retweets": 0.177478746064152, "Type": "Retweets"}, {"Dates": "2020-03-24T00:00:00", "Retweets": 0.3637444020721072, "Type": "Retweets"}, {"Dates": "2020-03-25T00:00:00", "Retweets": 0.0872841614485918, "Type": "Retweets"}, {"Dates": "2020-03-26T00:00:00", "Retweets": 0.3239643387561365, "Type": "Retweets"}, {"Dates": "2020-03-27T00:00:00", "Retweets": 0.09072102880605597, "Type": "Retweets"}, {"Dates": "2020-03-28T00:00:00", "Retweets": 0.5623265694528262, "Type": "Retweets"}, {"Dates": "2020-03-29T00:00:00", "Retweets": 0.3713828362073762, "Type": "Retweets"}, {"Dates": "2020-03-30T00:00:00", "Retweets": 0.24065062224561976, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-4f7d441c7b884b34b955cecd0ccdc0b3"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-4f7d441c7b884b34b955cecd0ccdc0b3") {
      outputDiv = document.getElementById("altair-viz-4f7d441c7b884b34b955cecd0ccdc0b3");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-0330b59d8bde7094475511e1ba004c5d"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#609048"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-2895a0d8ee3eba23e4bbf686509e8f89"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#AA4499"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-0330b59d8bde7094475511e1ba004c5d": [{"Dates": "2020-04-01T00:00:00", "Likes": 0.2407640665376774, "Type": "Likes"}, {"Dates": "2020-04-02T00:00:00", "Likes": 0.07126439766780507, "Type": "Likes"}, {"Dates": "2020-04-03T00:00:00", "Likes": 0.21679717089344536, "Type": "Likes"}, {"Dates": "2020-04-04T00:00:00", "Likes": 0.22748856194297637, "Type": "Likes"}, {"Dates": "2020-04-05T00:00:00", "Likes": 0.16770334203361512, "Type": "Likes"}, {"Dates": "2020-04-06T00:00:00", "Likes": 0.37829777471897225, "Type": "Likes"}, {"Dates": "2020-04-07T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-04-08T00:00:00", "Likes": 0.24812251381873116, "Type": "Likes"}, {"Dates": "2020-04-09T00:00:00", "Likes": 0.24952927579893258, "Type": "Likes"}, {"Dates": "2020-04-10T00:00:00", "Likes": 0.3654291489739295, "Type": "Likes"}, {"Dates": "2020-04-11T00:00:00", "Likes": 0.09111056283464704, "Type": "Likes"}, {"Dates": "2020-04-12T00:00:00", "Likes": 0.3836737697325421, "Type": "Likes"}, {"Dates": "2020-04-13T00:00:00", "Likes": 0.2758855025603068, "Type": "Likes"}, {"Dates": "2020-04-14T00:00:00", "Likes": 0.23531015855289641, "Type": "Likes"}, {"Dates": "2020-04-15T00:00:00", "Likes": 0.20595428239989266, "Type": "Likes"}, {"Dates": "2020-04-16T00:00:00", "Likes": 0.04978206010552879, "Type": "Likes"}, {"Dates": "2020-04-17T00:00:00", "Likes": 0.11832383227934397, "Type": "Likes"}, {"Dates": "2020-04-18T00:00:00", "Likes": 0.9531050483276846, "Type": "Likes"}, {"Dates": "2020-04-19T00:00:00", "Likes": 0.43685370108255744, "Type": "Likes"}, {"Dates": "2020-04-20T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-04-21T00:00:00", "Likes": 0.17760694637423333, "Type": "Likes"}, {"Dates": "2020-04-22T00:00:00", "Likes": 0.24214918602587576, "Type": "Likes"}, {"Dates": "2020-04-23T00:00:00", "Likes": 0.0663645374783034, "Type": "Likes"}, {"Dates": "2020-04-24T00:00:00", "Likes": 0.38338808883810116, "Type": "Likes"}, {"Dates": "2020-04-25T00:00:00", "Likes": 0.26942738294658203, "Type": "Likes"}, {"Dates": "2020-04-26T00:00:00", "Likes": 0.7218377072809672, "Type": "Likes"}, {"Dates": "2020-04-27T00:00:00", "Likes": 0.2246360814969679, "Type": "Likes"}, {"Dates": "2020-04-28T00:00:00", "Likes": 0.14898691494933491, "Type": "Likes"}, {"Dates": "2020-04-29T00:00:00", "Likes": 0.008263103446783276, "Type": "Likes"}], "data-2895a0d8ee3eba23e4bbf686509e8f89": [{"Dates": "2020-04-01T00:00:00", "Retweets": 0.19797093750202452, "Type": "Retweets"}, {"Dates": "2020-04-02T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-04-03T00:00:00", "Retweets": 0.6071768692058022, "Type": "Retweets"}, {"Dates": "2020-04-04T00:00:00", "Retweets": 0.24290054872794883, "Type": "Retweets"}, {"Dates": "2020-04-05T00:00:00", "Retweets": 0.12981724184844226, "Type": "Retweets"}, {"Dates": "2020-04-06T00:00:00", "Retweets": 0.5526292944278524, "Type": "Retweets"}, {"Dates": "2020-04-07T00:00:00", "Retweets": 0.35515201772514365, "Type": "Retweets"}, {"Dates": "2020-04-08T00:00:00", "Retweets": 0.276946299811476, "Type": "Retweets"}, {"Dates": "2020-04-09T00:00:00", "Retweets": 0.08160433281289478, "Type": "Retweets"}, {"Dates": "2020-04-10T00:00:00", "Retweets": 0.23087517896823598, "Type": "Retweets"}, {"Dates": "2020-04-11T00:00:00", "Retweets": 0.2800520870449672, "Type": "Retweets"}, {"Dates": "2020-04-12T00:00:00", "Retweets": 0.19695381485776478, "Type": "Retweets"}, {"Dates": "2020-04-13T00:00:00", "Retweets": 0.06725707288947051, "Type": "Retweets"}, {"Dates": "2020-04-14T00:00:00", "Retweets": 0.3224356524161522, "Type": "Retweets"}, {"Dates": "2020-04-15T00:00:00", "Retweets": 0.28336777729549034, "Type": "Retweets"}, {"Dates": "2020-04-16T00:00:00", "Retweets": 0.12517346152101946, "Type": "Retweets"}, {"Dates": "2020-04-17T00:00:00", "Retweets": 0.09931781519464618, "Type": "Retweets"}, {"Dates": "2020-04-18T00:00:00", "Retweets": 0.22834079439222063, "Type": "Retweets"}, {"Dates": "2020-04-19T00:00:00", "Retweets": 0.15595794165473545, "Type": "Retweets"}, {"Dates": "2020-04-20T00:00:00", "Retweets": 0.1534093044047241, "Type": "Retweets"}, {"Dates": "2020-04-21T00:00:00", "Retweets": 0.05952175800255252, "Type": "Retweets"}, {"Dates": "2020-04-22T00:00:00", "Retweets": 0.06505438690827109, "Type": "Retweets"}, {"Dates": "2020-04-23T00:00:00", "Retweets": 0.20354762012736707, "Type": "Retweets"}, {"Dates": "2020-04-24T00:00:00", "Retweets": 0.26823921169755827, "Type": "Retweets"}, {"Dates": "2020-04-25T00:00:00", "Retweets": 0.43547231418076277, "Type": "Retweets"}, {"Dates": "2020-04-26T00:00:00", "Retweets": 0.10266848928134131, "Type": "Retweets"}, {"Dates": "2020-04-27T00:00:00", "Retweets": 0.3503061085665049, "Type": "Retweets"}, {"Dates": "2020-04-28T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-04-29T00:00:00", "Retweets": 0.23635209287560655, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-6f1e2c71a7334d4abd9cb3d5ccff22d2"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-6f1e2c71a7334d4abd9cb3d5ccff22d2") {
      outputDiv = document.getElementById("altair-viz-6f1e2c71a7334d4abd9cb3d5ccff22d2");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-08593e449e10a3932922df0a598b10c6"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#117733"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-6128dcd03569cd20c59a9e26d3944f6b"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#9A1557"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-08593e449e10a3932922df0a598b10c6": [{"Dates": "2020-05-01T00:00:00", "Likes": 0.018294701986754966, "Type": "Likes"}, {"Dates": "2020-05-02T00:00:00", "Likes": 0.09718543046357615, "Type": "Likes"}, {"Dates": "2020-05-03T00:00:00", "Likes": 0.02384105960264901, "Type": "Likes"}, {"Dates": "2020-05-04T00:00:00", "Likes": 0.03708609271523179, "Type": "Likes"}, {"Dates": "2020-05-05T00:00:00", "Likes": 0.018211920529801324, "Type": "Likes"}, {"Dates": "2020-05-06T00:00:00", "Likes": 0.03360927152317881, "Type": "Likes"}, {"Dates": "2020-05-07T00:00:00", "Likes": 0.05347682119205298, "Type": "Likes"}, {"Dates": "2020-05-08T00:00:00", "Likes": 0.03741721854304636, "Type": "Likes"}, {"Dates": "2020-05-09T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-05-10T00:00:00", "Likes": 0.02293046357615894, "Type": "Likes"}, {"Dates": "2020-05-11T00:00:00", "Likes": 0.06639072847682119, "Type": "Likes"}, {"Dates": "2020-05-12T00:00:00", "Likes": 0.3753311258278146, "Type": "Likes"}, {"Dates": "2020-05-13T00:00:00", "Likes": 0.009105960264900662, "Type": "Likes"}, {"Dates": "2020-05-14T00:00:00", "Likes": 0.16026490066225166, "Type": "Likes"}, {"Dates": "2020-05-15T00:00:00", "Likes": 0.021688741721854303, "Type": "Likes"}, {"Dates": "2020-05-16T00:00:00", "Likes": 0.01597682119205298, "Type": "Likes"}, {"Dates": "2020-05-17T00:00:00", "Likes": 0.07980132450331126, "Type": "Likes"}, {"Dates": "2020-05-18T00:00:00", "Likes": 0.03799668874172185, "Type": "Likes"}, {"Dates": "2020-05-19T00:00:00", "Likes": 0.010513245033112583, "Type": "Likes"}, {"Dates": "2020-05-20T00:00:00", "Likes": 0.03137417218543046, "Type": "Likes"}, {"Dates": "2020-05-21T00:00:00", "Likes": 0.0097682119205298, "Type": "Likes"}, {"Dates": "2020-05-22T00:00:00", "Likes": 0.02533112582781457, "Type": "Likes"}, {"Dates": "2020-05-23T00:00:00", "Likes": 0.011175496688741722, "Type": "Likes"}, {"Dates": "2020-05-24T00:00:00", "Likes": 0.029221854304635763, "Type": "Likes"}, {"Dates": "2020-05-25T00:00:00", "Likes": 0.017135761589403973, "Type": "Likes"}, {"Dates": "2020-05-26T00:00:00", "Likes": 0.14304635761589404, "Type": "Likes"}, {"Dates": "2020-05-27T00:00:00", "Likes": 0.17938741721854304, "Type": "Likes"}, {"Dates": "2020-05-28T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-05-29T00:00:00", "Likes": 0.001986754966887417, "Type": "Likes"}, {"Dates": "2020-05-30T00:00:00", "Likes": 0.048344370860927154, "Type": "Likes"}], "data-6128dcd03569cd20c59a9e26d3944f6b": [{"Dates": "2020-05-01T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-05-02T00:00:00", "Retweets": 0.036053199735513984, "Type": "Retweets"}, {"Dates": "2020-05-03T00:00:00", "Retweets": 0.08801736829379866, "Type": "Retweets"}, {"Dates": "2020-05-04T00:00:00", "Retweets": 0.09369567249844708, "Type": "Retweets"}, {"Dates": "2020-05-05T00:00:00", "Retweets": 0.025265125310870513, "Type": "Retweets"}, {"Dates": "2020-05-06T00:00:00", "Retweets": 0.01349219632309237, "Type": "Retweets"}, {"Dates": "2020-05-07T00:00:00", "Retweets": 0.03581953524443917, "Type": "Retweets"}, {"Dates": "2020-05-08T00:00:00", "Retweets": 0.027185720244748333, "Type": "Retweets"}, {"Dates": "2020-05-09T00:00:00", "Retweets": 0.01004554360413474, "Type": "Retweets"}, {"Dates": "2020-05-10T00:00:00", "Retweets": 0.06868788931961149, "Type": "Retweets"}, {"Dates": "2020-05-11T00:00:00", "Retweets": 0.20815825972856764, "Type": "Retweets"}, {"Dates": "2020-05-12T00:00:00", "Retweets": 0.2155903329739293, "Type": "Retweets"}, {"Dates": "2020-05-13T00:00:00", "Retweets": 0.11840241138507569, "Type": "Retweets"}, {"Dates": "2020-05-14T00:00:00", "Retweets": 0.06506994578090822, "Type": "Retweets"}, {"Dates": "2020-05-15T00:00:00", "Retweets": 0.09399144005924011, "Type": "Retweets"}, {"Dates": "2020-05-16T00:00:00", "Retweets": 0.04773020045220235, "Type": "Retweets"}, {"Dates": "2020-05-17T00:00:00", "Retweets": 0.1287058383244673, "Type": "Retweets"}, {"Dates": "2020-05-18T00:00:00", "Retweets": 0.15699155411781912, "Type": "Retweets"}, {"Dates": "2020-05-19T00:00:00", "Retweets": 0.1037256565099509, "Type": "Retweets"}, {"Dates": "2020-05-20T00:00:00", "Retweets": 0.10719057483764918, "Type": "Retweets"}, {"Dates": "2020-05-21T00:00:00", "Retweets": 0.0055293380178080215, "Type": "Retweets"}, {"Dates": "2020-05-22T00:00:00", "Retweets": 0.01258053949572578, "Type": "Retweets"}, {"Dates": "2020-05-23T00:00:00", "Retweets": 0.09521212392633738, "Type": "Retweets"}, {"Dates": "2020-05-24T00:00:00", "Retweets": 0.30219272544395237, "Type": "Retweets"}, {"Dates": "2020-05-25T00:00:00", "Retweets": 0.2081666483785078, "Type": "Retweets"}, {"Dates": "2020-05-26T00:00:00", "Retweets": 0.14955393353943253, "Type": "Retweets"}, {"Dates": "2020-05-27T00:00:00", "Retweets": 0.1486346998669587, "Type": "Retweets"}, {"Dates": "2020-05-28T00:00:00", "Retweets": 0.40675914115919504, "Type": "Retweets"}, {"Dates": "2020-05-29T00:00:00", "Retweets": 0.20900240145399657, "Type": "Retweets"}, {"Dates": "2020-05-30T00:00:00", "Retweets": 1.0, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-653022c0cab64f0dbfa7dc3af810cb4f"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-653022c0cab64f0dbfa7dc3af810cb4f") {
      outputDiv = document.getElementById("altair-viz-653022c0cab64f0dbfa7dc3af810cb4f");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-5139b561f84ef75ee238e50372cb3cf6"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#00C000"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-e476b60f78b496a05d0c7d70249690da"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#D2458B"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-5139b561f84ef75ee238e50372cb3cf6": [{"Dates": "2020-06-01T00:00:00", "Likes": 0.05299707602339181, "Type": "Likes"}, {"Dates": "2020-06-02T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-06-03T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-06-04T00:00:00", "Likes": 0.05263157894736842, "Type": "Likes"}, {"Dates": "2020-06-05T00:00:00", "Likes": 0.06944444444444445, "Type": "Likes"}, {"Dates": "2020-06-06T00:00:00", "Likes": 0.34502923976608185, "Type": "Likes"}, {"Dates": "2020-06-07T00:00:00", "Likes": 0.0581140350877193, "Type": "Likes"}, {"Dates": "2020-06-08T00:00:00", "Likes": 0.19809941520467836, "Type": "Likes"}, {"Dates": "2020-06-09T00:00:00", "Likes": 0.22880116959064328, "Type": "Likes"}, {"Dates": "2020-06-10T00:00:00", "Likes": 0.16337719298245615, "Type": "Likes"}, {"Dates": "2020-06-11T00:00:00", "Likes": 0.11257309941520467, "Type": "Likes"}, {"Dates": "2020-06-12T00:00:00", "Likes": 0.9155701754385965, "Type": "Likes"}, {"Dates": "2020-06-13T00:00:00", "Likes": 0.06542397660818713, "Type": "Likes"}, {"Dates": "2020-06-14T00:00:00", "Likes": 0.4470029239766082, "Type": "Likes"}, {"Dates": "2020-06-15T00:00:00", "Likes": 0.09978070175438597, "Type": "Likes"}, {"Dates": "2020-06-16T00:00:00", "Likes": 0.18128654970760233, "Type": "Likes"}, {"Dates": "2020-06-17T00:00:00", "Likes": 0.10782163742690058, "Type": "Likes"}, {"Dates": "2020-06-18T00:00:00", "Likes": 0.04532163742690058, "Type": "Likes"}, {"Dates": "2020-06-19T00:00:00", "Likes": 0.08406432748538012, "Type": "Likes"}, {"Dates": "2020-06-20T00:00:00", "Likes": 0.1597222222222222, "Type": "Likes"}, {"Dates": "2020-06-21T00:00:00", "Likes": 0.03764619883040936, "Type": "Likes"}, {"Dates": "2020-06-22T00:00:00", "Likes": 0.08589181286549707, "Type": "Likes"}, {"Dates": "2020-06-23T00:00:00", "Likes": 0.028143274853801168, "Type": "Likes"}, {"Dates": "2020-06-24T00:00:00", "Likes": 0.13669590643274854, "Type": "Likes"}, {"Dates": "2020-06-25T00:00:00", "Likes": 0.06907894736842106, "Type": "Likes"}, {"Dates": "2020-06-26T00:00:00", "Likes": 0.13779239766081872, "Type": "Likes"}, {"Dates": "2020-06-27T00:00:00", "Likes": 0.09283625730994152, "Type": "Likes"}, {"Dates": "2020-06-28T00:00:00", "Likes": 0.30701754385964913, "Type": "Likes"}, {"Dates": "2020-06-29T00:00:00", "Likes": 0.18311403508771928, "Type": "Likes"}], "data-e476b60f78b496a05d0c7d70249690da": [{"Dates": "2020-06-01T00:00:00", "Retweets": 0.7950410823729142, "Type": "Retweets"}, {"Dates": "2020-06-02T00:00:00", "Retweets": 0.535730801938874, "Type": "Retweets"}, {"Dates": "2020-06-03T00:00:00", "Retweets": 0.4779970947256514, "Type": "Retweets"}, {"Dates": "2020-06-04T00:00:00", "Retweets": 0.34450673410921784, "Type": "Retweets"}, {"Dates": "2020-06-05T00:00:00", "Retweets": 0.3200487343666256, "Type": "Retweets"}, {"Dates": "2020-06-06T00:00:00", "Retweets": 0.6651588301311319, "Type": "Retweets"}, {"Dates": "2020-06-07T00:00:00", "Retweets": 0.6058456265432585, "Type": "Retweets"}, {"Dates": "2020-06-08T00:00:00", "Retweets": 0.1466838593520276, "Type": "Retweets"}, {"Dates": "2020-06-09T00:00:00", "Retweets": 0.0937251097353368, "Type": "Retweets"}, {"Dates": "2020-06-10T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-06-11T00:00:00", "Retweets": 0.02454356584751666, "Type": "Retweets"}, {"Dates": "2020-06-12T00:00:00", "Retweets": 0.10330638497680562, "Type": "Retweets"}, {"Dates": "2020-06-13T00:00:00", "Retweets": 0.5660986808487873, "Type": "Retweets"}, {"Dates": "2020-06-14T00:00:00", "Retweets": 0.8380944556143923, "Type": "Retweets"}, {"Dates": "2020-06-15T00:00:00", "Retweets": 0.29600380747881816, "Type": "Retweets"}, {"Dates": "2020-06-16T00:00:00", "Retweets": 0.04627664699497657, "Type": "Retweets"}, {"Dates": "2020-06-17T00:00:00", "Retweets": 0.21770670635344647, "Type": "Retweets"}, {"Dates": "2020-06-18T00:00:00", "Retweets": 0.29431533138844274, "Type": "Retweets"}, {"Dates": "2020-06-19T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-06-20T00:00:00", "Retweets": 0.8555341900444475, "Type": "Retweets"}, {"Dates": "2020-06-21T00:00:00", "Retweets": 0.7423933790281876, "Type": "Retweets"}, {"Dates": "2020-06-22T00:00:00", "Retweets": 0.3807207787849414, "Type": "Retweets"}, {"Dates": "2020-06-23T00:00:00", "Retweets": 0.4875003245977861, "Type": "Retweets"}, {"Dates": "2020-06-24T00:00:00", "Retweets": 0.47469449849677525, "Type": "Retweets"}, {"Dates": "2020-06-25T00:00:00", "Retweets": 0.35815857201381035, "Type": "Retweets"}, {"Dates": "2020-06-26T00:00:00", "Retweets": 0.8764150157587791, "Type": "Retweets"}, {"Dates": "2020-06-27T00:00:00", "Retweets": 0.34538850488202166, "Type": "Retweets"}, {"Dates": "2020-06-28T00:00:00", "Retweets": 0.7957376727693889, "Type": "Retweets"}, {"Dates": "2020-06-29T00:00:00", "Retweets": 0.7053073547259948, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



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





<div id="altair-viz-4e12136ffe574b5ba359c479ec0e3553"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-4e12136ffe574b5ba359c479ec0e3553") {
      outputDiv = document.getElementById("altair-viz-4e12136ffe574b5ba359c479ec0e3553");
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
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}, "axis": {"labelFontSize": 13, "titleFontSize": 15, "titlePadding": 15}, "header": {"labelFontSize": 12, "titleFontSize": 15}, "legend": {"labelFontSize": 12, "titleFontSize": 15, "titlePadding": 10}}, "hconcat": [{"data": {"name": "data-2ec52c4ea60606e51c99792cf3ce8b5e"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#00FF7F"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Likes", "title": "Norm. Count"}}, "height": 130, "width": 280}, {"data": {"name": "data-a8d0b6560b62ed016e4369504e1761bc"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "Type", "scale": {"range": ["#FF83A8"]}}, "x": {"type": "temporal", "field": "Dates", "timeUnit": "monthdate", "title": "Dates"}, "y": {"type": "quantitative", "field": "Retweets", "title": "Norm. Count"}}, "height": 130, "width": 280}], "resolve": {"scale": {"color": "independent"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-2ec52c4ea60606e51c99792cf3ce8b5e": [{"Dates": "2020-07-01T00:00:00", "Likes": 0.5591918042117245, "Type": "Likes"}, {"Dates": "2020-07-02T00:00:00", "Likes": 1.0, "Type": "Likes"}, {"Dates": "2020-07-03T00:00:00", "Likes": 0.09704040978941378, "Type": "Likes"}, {"Dates": "2020-07-04T00:00:00", "Likes": 0.7199772339214571, "Type": "Likes"}, {"Dates": "2020-07-05T00:00:00", "Likes": 0.26124075128059193, "Type": "Likes"}, {"Dates": "2020-07-06T00:00:00", "Likes": 0.1553784860557769, "Type": "Likes"}, {"Dates": "2020-07-07T00:00:00", "Likes": 0.12208309618668184, "Type": "Likes"}, {"Dates": "2020-07-08T00:00:00", "Likes": 0.2740466704610131, "Type": "Likes"}, {"Dates": "2020-07-09T00:00:00", "Likes": 0.10017074558907228, "Type": "Likes"}, {"Dates": "2020-07-10T00:00:00", "Likes": 0.10700056915196357, "Type": "Likes"}, {"Dates": "2020-07-11T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-12T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-13T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-14T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-15T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-16T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-17T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-18T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-19T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-20T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-21T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-22T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-23T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-24T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-25T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-26T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-27T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-28T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-29T00:00:00", "Likes": 0.0, "Type": "Likes"}, {"Dates": "2020-07-30T00:00:00", "Likes": 0.0, "Type": "Likes"}], "data-a8d0b6560b62ed016e4369504e1761bc": [{"Dates": "2020-07-01T00:00:00", "Retweets": 0.6670585181855079, "Type": "Retweets"}, {"Dates": "2020-07-02T00:00:00", "Retweets": 1.0, "Type": "Retweets"}, {"Dates": "2020-07-03T00:00:00", "Retweets": 0.5334619237514988, "Type": "Retweets"}, {"Dates": "2020-07-04T00:00:00", "Retweets": 0.6311493156226599, "Type": "Retweets"}, {"Dates": "2020-07-05T00:00:00", "Retweets": 0.6286095086506381, "Type": "Retweets"}, {"Dates": "2020-07-06T00:00:00", "Retweets": 0.5623421310675466, "Type": "Retweets"}, {"Dates": "2020-07-07T00:00:00", "Retweets": 0.7084912712343024, "Type": "Retweets"}, {"Dates": "2020-07-08T00:00:00", "Retweets": 0.3330548660543145, "Type": "Retweets"}, {"Dates": "2020-07-09T00:00:00", "Retweets": 0.42598376139056415, "Type": "Retweets"}, {"Dates": "2020-07-10T00:00:00", "Retweets": 0.6838557725985549, "Type": "Retweets"}, {"Dates": "2020-07-11T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-12T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-13T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-14T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-15T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-16T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-17T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-18T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-19T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-20T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-21T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-22T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-23T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-24T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-25T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-26T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-27T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-28T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-29T00:00:00", "Retweets": 0.0, "Type": "Retweets"}, {"Dates": "2020-07-30T00:00:00", "Retweets": 0.0, "Type": "Retweets"}]}}, {"mode": "vega-lite"});
</script>



# Recap

## January 2020

![1_jan2020.png](attachment:1_jan2020.png)

## February 2020

![2_feb2020.png](attachment:2_feb2020.png)

## March 2020

![3_mar2020.png](attachment:3_mar2020.png)

## April 2020

![4_apr2020.png](attachment:4_apr2020.png)

## May 2020

![5_may2020.png](attachment:5_may2020.png)

## June 2020

![6_june2020.png](attachment:6_june2020.png)

## July 2020

![7_jul2020.png](attachment:7_jul2020.png)
