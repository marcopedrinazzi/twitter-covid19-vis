import pandas as pd
import numpy as np
import json
import itertools  
from collections import Counter
#import emoji_data_python
import altair as alt

import demoji

#demoji.download_codes()

data = []
with open('general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index= 0
emos = []
for element in data:
    em = demoji.findall_list(data[index]['full_text'], False)
    emos.append(em)
    index= index+1

merged=list(itertools.chain.from_iterable(emos))
c = Counter(merged)

df = pd.DataFrame.from_dict(c, orient='index').reset_index()
df = df.rename(columns={'index':'emoji', 0:'count'})


chart = alt.Chart(
    df
).mark_bar().encode(
    x=alt.X('count:Q'),
    y=alt.Y('emoji:N',sort='-x'),
    color=alt.Color('count:Q',scale=alt.Scale(scheme="blues"))
).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).transform_filter(
    (alt.datum.rank < 15)
).properties(width=700, height=300,  title = "Most frequent emojis in the dataset")

chart.show()