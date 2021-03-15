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

index=0
new = []
for element in data: 
    token=data[index]['created_at']
    #new.append(token[0:10]) Data completa
    new.append(token[4:7])#il 7 è escluso
    index=index+1

print(new)
count=Counter(new)
#https://altair-viz.github.io/user_guide/data.html
df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'month', 0:'tweet count'})
print(df)

chart = alt.Chart(df).mark_bar().encode(
    x='tweet count',
    y=alt.X('month',sort = ['Jan','Feb','Mar','Apr','May','Jun','Jul'])
)

chart.show()