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
from PIL import Image
import nltk
from nltk.corpus import stopwords


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

def noamp(text):
    clean = re.sub("&amp", " ",text)
    return (clean)


data = []
with open('../dataset/general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
comment_words = ''
stop_words = stopwords.words('english')
for element in data:
    data[index]['full_text'] = data[index]['full_text'].lower()#new - metto tutto minuscolo
    #data[index]['full_text'] = contractions.fix(data[index]['full_text'])
    data[index]['full_text'] = re.sub("\'\w+", '', data[index]['full_text'])#new - rimuove tutto quello dopo '
    data[index]['full_text'] = remove_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_twitter_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_emoticons(data[index]['full_text'])
    data[index]['full_text'] = remove_emoji(data[index]['full_text'])
    data[index]['full_text'] = give_emoji_free_text(data[index]['full_text'])
    data[index]['full_text'] = noamp(data[index]['full_text'])#new - no amp con lo spazio
    data[index]['full_text'] = re.sub("#\S+", " ",  data[index]['full_text'])#new - remove hashtag
    data[index]['full_text'] = re.sub("@\S+", " ",  data[index]['full_text'])#new - no mentions
    data[index]['full_text'] = data[index]['full_text'].translate(str.maketrans('', '', string.punctuation))#new - no puntuaction
    data[index]['full_text'] = data[index]['full_text'].encode('ascii', 'ignore').decode()#new - no unicode
    data[index]['full_text'] = re.sub("^rt ", " ", data[index]['full_text'])#new - no RT
    data[index]['full_text'] = re.sub('\s{2,}', " ", data[index]['full_text'])#new - remove big spaces

    
    tokens=data[index]['full_text'].split()

    comment_words += " ".join(tokens)+" "
    index=index+1

mask= np.array(Image.open('face_mask.jpg'))

wordcloud = WordCloud(background_color ='black',
            mask=mask,
            width=mask.shape[1],
            height=mask.shape[0],
            stopwords = stop_words,
            normalize_plurals=False,
            min_word_length = 3,
            max_words=400,
            font_path = 'GothamMedium.ttf',
            min_font_size = 10).generate(comment_words) 
  
#plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud,interpolation="bilinear") 
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 
