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
with open('fakecovid_result_translated_full.json', 'r') as f:
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
out = dict(itertools.islice(fdist_sorted.items(), 15))

df = pd.DataFrame.from_dict(out, orient='index').reset_index()
df = df.rename(columns={'index':'words', 0:'count'})
print(df)

chart = alt.Chart(df).mark_bar().encode(
    x='count',
    y='words',
)

chart.show()