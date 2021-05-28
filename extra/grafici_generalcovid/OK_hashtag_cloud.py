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
from PIL import Image

data = []
with open('../dataset/general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
#new = []
comment_words = ''
#stopwords = set(STOPWORDS)
cmt_list = []
#printable = set(string.printable)
for element in data:
    for entity in data[index]['entities']['hashtags']:
        entity['text'] = entity['text'].lower()
        token=entity['text']
        cmt_list.append(token)
        
    index=index+1

fdist = dict(nltk.FreqDist(cmt_list))
print(fdist)

mask= np.array(Image.open('covid.jpg'))

wordcloud = WordCloud(mask=mask,
            width=mask.shape[1],
            height=mask.shape[0],
               background_color ='black', 
                min_word_length = 3,
                max_words=450,
                font_path = 'GothamMedium.ttf',
               min_font_size = 10).generate_from_frequencies(fdist) 

#plot the WordCloud image                        

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 
