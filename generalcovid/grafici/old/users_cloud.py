import pandas as pd
import numpy as np
import json
import sys
import string
import re
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import nltk

data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
cmt_list = []
#stopwords = set(STOPWORDS) 
for element in data:
    token=data[index]['user']['screen_name']
    cmt_list.append(token)
    index=index+1

fdist = dict(nltk.FreqDist(cmt_list))
#print(fdist)

wordcloud = WordCloud(width = 800, height = 800, 
               background_color ='white', 
                font_path = 'GothamMedium.ttf',
                min_word_length = 3,
               min_font_size = 10).generate_from_frequencies(fdist) 


#plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 