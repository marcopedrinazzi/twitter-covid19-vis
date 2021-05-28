import pandas as pd
import json
from collections import Counter
import altair as alt

data = []
with open('dataset/fakecovid_result_translated_full.json','r') as f:
    for line in f:
        data.append(json.loads(line))

index = 0
new = []
for element in data:
    token = data[index]['created_at']
    new.append(token[4:7])
    index = index + 1

print(new)
#print(len(new))

count = Counter(new)
#print(count)

df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'Month',0:'Tweet count'})

#print(df)

chart = alt.Chart(df).mark_area(
    point= True,
    line={'color':'dodgerblue'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='mediumturquoise', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).properties(width=500, height=300,  title = "Trend of the number of Tweets during the year").encode(
    alt.X('Month', sort = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']),
    alt.Y('Tweet count:Q'),
    tooltip=['Month', 'Tweet count']
).interactive()

chart.show()
