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


data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
comment_words = ''
stopwords = set(STOPWORDS) 
for element in data:
    token=data[index]['user']['screen_name']
    comment_words += token + " "
    index=index+1

wordcloud = WordCloud(width = 800, height = 800, 
               background_color ='white', 
                stopwords = stopwords, 
                normalize_plurals=False,
                min_word_length = 3,
               min_font_size = 10).generate(comment_words) 
  
#plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 