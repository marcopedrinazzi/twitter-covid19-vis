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
    new.append(token[0:3])
    index = index + 1

print(new)
#print(len(new))

count = Counter(new)
#print(count)

df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'Day',0:'Tweet count'})

#print(df)

chart = alt.Chart(df).mark_bar().encode(
    x = alt.X('Tweet count:Q'),
    y = alt.Y('Day', sort = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']),
    color=alt.Color('Tweet count:Q',scale=alt.Scale(scheme="blues"))
).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).properties(width=700, height=300,  title = "Number of Tweets per day of the week")

chart.show()
