import pandas as pd
import numpy as np
import json
import sys
import string
import re
# This will load the fields list
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk 

data = []
with open('fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
#comment_words = ''
stopwords = set(STOPWORDS)
cmt_list = []
for element in data:
    for entity in data[index]['entities']['user_mentions']:
        token=entity['screen_name']
        cmt_list.append(token)
    index=index+1


fdist = dict(nltk.FreqDist(cmt_list))
print(fdist)

wordcloud = WordCloud(width = 800, height = 800, 
               background_color ='white', 
                min_word_length = 3,
                font_path = 'GothamMedium.ttf',
               min_font_size = 10).generate_from_frequencies(fdist) 

#plot the WordCloud image                        

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 