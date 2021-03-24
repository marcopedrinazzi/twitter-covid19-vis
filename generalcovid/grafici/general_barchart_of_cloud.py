import pandas as pd
import numpy as np
import json
import sys
import string
import re
import itertools  
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import nltk
from PIL import Image
import altair as alt

data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
#comment_words = ''
cmt_list = []
stopwords = set(STOPWORDS) 
for element in data:
    token=data[index]['user']['screen_name']
    cmt_list.append(token)
    #comment_words += token + " "
    index=index+1

fdist = dict(nltk.FreqDist(cmt_list))
fdist_sorted = dict(sorted(fdist.items(), key=lambda item: item[1], reverse=True))
print(fdist_sorted)

df = pd.DataFrame.from_dict(fdist_sorted, orient='index').reset_index()
df = df.rename(columns={'index':'usernames', 0:'count'})
print(df)

alt.data_transformers.disable_max_rows()

chart = alt.Chart(
    df,
).mark_bar().encode(
    x=alt.X('usernames:N', sort='-y'),
    y=alt.Y('count:Q'),
    color=alt.Color('count:Q')

).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).transform_filter(
    (alt.datum.rank < 20)
)

chart.show()