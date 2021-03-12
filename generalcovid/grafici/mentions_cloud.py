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

def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
    return emoticon_pattern.sub(r'', text)

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_urls(text):
    result = re.sub(r"http\S+", "", text)
    return(result)

def remove_twitter_urls(text):
    clean = re.sub(r"pic.twitter\S+", "",text)
    return(clean)

def give_emoji_free_text(text):
    return emoji.get_emoji_regexp().sub(r'', text)


data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
comment_words = ''
stopwords = set(STOPWORDS) 
for element in data:
    for entity in data[index]['entities']['user_mentions']:
        token=entity['screen_name']
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