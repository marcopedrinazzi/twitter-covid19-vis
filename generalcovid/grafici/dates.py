import pandas as pd
import numpy as np
import json
import sys
import string
import re
from collections import Counter
import altair as alt

data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

data_fake = []
with open('fakecovid_result.json', 'r') as f1:
    for line in f1:
        data_fake.append(json.loads(line))

index=0
new = []
for element in data: 
    token=data[index]['created_at']
    #new.append(token[0:10]) Data completa
    new.append(token[4:7])#il 7 è escluso
    index=index+1

index_fake=0
new_fake = []
for element in data_fake: 
    token_fake=data_fake[index_fake]['created_at']
    #new.append(token[0:10]) Data completa
    new_fake.append(token_fake[4:7])#il 7 è escluso
    index_fake=index_fake+1

print(new)
count=Counter(new)
#https://altair-viz.github.io/user_guide/data.html
df1 = pd.DataFrame.from_dict(count, orient='index').reset_index()
df1 = df1.rename(columns={'index':'month', 0:'tweet count'})
df1['dataset'] = 'general'
print(df1)

print(new_fake)
count_fake=Counter(new_fake)
#https://altair-viz.github.io/user_guide/data.html
df2 = pd.DataFrame.from_dict(count_fake, orient='index').reset_index()
df2 = df2.rename(columns={'index':'month', 0:'tweet count'})
df2['dataset'] = 'fake'
print(df2)
frames = [df1, df2]
result = pd.concat(frames)

#chart = alt.Chart(df).mark_bar().encode(
#    x='tweet count',
#    y=alt.Y('month',sort = ['Jan','Feb','Mar','Apr','May','Jun','Jul'])
#)

#chart = alt.Chart(result).mark_line().encode( 
#    x=alt.X('month',sort = ['Jan','Feb','Mar','Apr','May','Jun','Jul']),
#    y='tweet count',
#    color='dataset',
#)

#chart = alt.Chart(result).mark_bar(opacity=0.7).encode(
#    x=alt.X('month',sort = ['Jan','Feb','Mar','Apr','May','Jun','Jul'],stack=None),
#    y='tweet count',
#    color="dataset",
#)

chart.show()

