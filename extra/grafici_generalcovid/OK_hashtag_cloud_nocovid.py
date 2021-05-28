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
cmt_list = []
#stopwords = ["covid19", "coronavirus", "corona", "covid_19", "covid","coronavirusoutbreak","covid2019", "virus", "covid 19", "covid__19"] + list(STOPWORDS)
stopwords = ["covid19", "coronavirus", "corona", "covid_19", "covid","coronavirusoutbreak","covid2019", "virus", "covid__19", "covidー19", "coronaviruspandemic"]
for element in data:
    for entity in data[index]['entities']['hashtags']:
        entity['text'] = entity['text'].lower()
        if entity['text'] not in stopwords:
            token=entity['text']
            cmt_list.append(token)
        
    index=index+1

fdist = dict(nltk.FreqDist(cmt_list))
print(fdist)

mask= np.array(Image.open('speech_bubble.jpg'))

wordcloud = WordCloud(mask=mask,
            width=mask.shape[1],
            height=mask.shape[0],
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
