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
print(fdist)

mask= np.array(Image.open('circle.jpg'))

wordcloud = WordCloud(background_color ='white', 
                font_path = 'GothamMedium.ttf',
                mask=mask,
                width=mask.shape[1],
                height=mask.shape[0],
                min_word_length = 3,
                max_words=400,
               min_font_size = 10).generate_from_frequencies(fdist) 


#plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
