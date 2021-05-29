# Bigrams and Trigrams Word Clouds - General Covid-19 dataset 

In order to create the word clouds and the bar charts, we need the following packages:


```python
from itertools import tee, islice 
import pandas as pd
import numpy as np
import json
#import sys
import string
import re
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder,TrigramCollocationFinder, TrigramAssocMeasures
from operator import itemgetter
import itertools
import contractions
from nltk.corpus import stopwords
import num2words
from PIL import Image
import altair as alt
import itertools
from matplotlib.colors import ListedColormap
from IPython.core.display import Image, display
alt.data_transformers.disable_max_rows()
```

Then we have defined the following functions to clean the tweets' text:


```python
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
```

To read the JSON file that has all the tweets, it is necessary to do:


```python
data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
data1 = data
```

## Bigrams

We're interested in the "full_text" field, that it has been cleaned with specific functions:


```python
index=0
stop_words = stopwords.words('english')
new_bigram=[]
for element in data:
    data[index]['full_text'] = data[index]['full_text'].lower()                              # Put everything in lowercase
    data[index]['full_text'] = contractions.fix(data[index]['full_text'])
    #data[index]['full_text'] = re.sub("\'\w+", '', data[index]['full_text'])                # Remove everything after '
    data[index]['full_text'] = remove_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_twitter_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_emoticons(data[index]['full_text'])
    data[index]['full_text'] = remove_emoji(data[index]['full_text'])
    data[index]['full_text'] = give_emoji_free_text(data[index]['full_text'])
    data[index]['full_text'] = noamp(data[index]['full_text'])                               # No amp with space
    data[index]['full_text'] = re.sub("#\S+", " ",  data[index]['full_text'])                # Remove hashtags
    data[index]['full_text'] = re.sub("@\S+", " ",  data[index]['full_text'])                # No mentions
    data[index]['full_text'] = data[index]['full_text'].translate(str.maketrans('', '', string.punctuation)) # No puntuaction
    data[index]['full_text'] = data[index]['full_text'].encode('ascii', 'ignore').decode()   # No unicode
    data[index]['full_text'] = re.sub("^rt ", " ", data[index]['full_text'])                 # No RT
    data[index]['full_text'] = re.sub('\s{2,}', " ", data[index]['full_text'])               # Remove big spaces
    bigram_tokens=list(nltk.bigrams(nltk.word_tokenize(data[index]['full_text'])))
    #print(bigram_tokens)
    clean_bigram_tokens = [gram for gram in bigram_tokens if not any(stop in gram for stop in stop_words)]
    new_bigram.append(clean_bigram_tokens)
    index=index+1
```

The dictionary is created:


```python
list_bi=list(itertools.chain.from_iterable(new_bigram))
fdist_bi = dict(nltk.FreqDist(list_bi))
bi = {}
for k,v in fdist_bi.items():
    bi[" ".join(k)] = fdist_bi[k]
    bi[" ".join(k)] = v

#for x, y in bi.items():
#    print(x, y)
```

Let's see the most frequent bigrams in the dataset


```python
df_bi = pd.DataFrame.from_dict(bi, orient='index').reset_index()
df_bi = df_bi.rename(columns={'index':'bigrams', 0:'count'})
#print(df)
#alt.renderers.enable('altair_viewer',inline=True)


chart = alt.Chart(
    df_bi
).mark_bar().encode(
    x=alt.X('count:Q',title="Tweet Count"),
    y=alt.Y('bigrams:N',sort='-x',title="Bigrams"),
    color=alt.Color('count:Q',scale=alt.Scale(scheme="reds"),title="Tweet Count")
).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).transform_filter(
    (alt.datum.rank < 10)
).properties(width=700, height=300, title = "The 10 most frequent bigrams in the dataset").configure_title(
    fontSize=17,
    offset=25
).configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    gradientThickness=20,
    titleFontSize=15,
    labelFontSize=13,
    titlePadding=10
)

chart
```

![img/bigrams_freq.png](attachment:img/bigrams_freq.png)

The word cloud is created:


```python
mask=np.array(Image.open('grafici/number_two.jpg'))
abi = ['#3C1067', '#075A23', '#44AA99', '#D55E00', '#AA4499', '#882255']
my_cmapbi = ListedColormap(abi)

wordcloud_bi = WordCloud(
            mask=mask,
            width=mask.shape[1],
            height=mask.shape[0],
            background_color ='white', 
            min_word_length = 3,
            max_words=300,
            font_path = 'grafici/GothamMedium.ttf',
            min_font_size = 15,
            colormap=my_cmapbi).generate_from_frequencies(bi)
```

Plot the word cloud:


```python
# Plot the word cloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_bi) 
plt.axis("off") 
plt.tight_layout(pad = 0)
#plt.show()
```

![cloud_bi_gen.png](attachment:cloud_bi_gen.png)

## Trigrams

We're interested in the "full_text" field, that it has been cleaned with specific functions:


```python
index_tri=0
stop_words_tri = stopwords.words('english')
new_trigram=[]
for element in data1:
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].lower()                   # Put everything in lowercase
    data1[index_tri]['full_text'] = contractions.fix(data1[index_tri]['full_text'])
    #data[index_tri]['full_text'] = re.sub("\'\w+", '', data[index_tri]['full_text'])     # Remove everything after '
    data1[index_tri]['full_text'] = remove_urls(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_twitter_urls(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_emoticons(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_emoji(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = give_emoji_free_text(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = noamp(data1[index_tri]['full_text'])                    # No amp with space
    data1[index_tri]['full_text'] = re.sub("#\S+", " ",  data1[index_tri]['full_text'])     # Remove hashtags
    data1[index_tri]['full_text'] = re.sub("@\S+", " ",  data1[index_tri]['full_text'])     # No mentions
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].translate(str.maketrans('', '', string.punctuation)) # No puntuaction
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].encode('ascii', 'ignore').decode() # No unicode
    data1[index_tri]['full_text'] = re.sub("^rt ", " ", data1[index_tri]['full_text'])      # No RT
    data1[index_tri]['full_text'] = re.sub(r'\b\d\b', lambda x: num2words.num2words(int(x.group(0))), data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = re.sub('\s{2,}', " ", data1[index_tri]['full_text'])    # Remove big spaces
    trigram_tokens=list(nltk.trigrams(nltk.word_tokenize(data1[index_tri]['full_text'])))
    #print(trigram_tokens)
    clean_trigram_tokens = [gram for gram in trigram_tokens if not any(stop in gram for stop in stop_words_tri)]
    new_trigram.append(clean_trigram_tokens)
    index_tri=index_tri+1
```

The dictionary is created:


```python
list_tri=list(itertools.chain.from_iterable(new_trigram))
fdist_tri = dict(nltk.FreqDist(list_tri))
tri = {}
for k,v in fdist_tri.items():
    tri[" ".join(k)] = fdist_tri[k]
    tri[" ".join(k)] = v

#for x, y in tri.items():
#    print(x, y)
```

Let's see the most frequent trigrams in the dataset:


```python
df_tri = pd.DataFrame.from_dict(tri, orient='index').reset_index()
df_tri = df_tri.rename(columns={'index':'trigrams', 0:'count'})
#print(df)
#alt.renderers.enable('altair_viewer',inline=True)

c = alt.Chart(
    df_tri
).mark_bar().encode(
    x=alt.X('count:Q',title="Tweet Count"),
    y=alt.Y('trigrams:N',sort='-x',title="Trigrams"),
    color=alt.Color('count:Q',scale=alt.Scale(scheme="blues"),title="Trigrams")
).transform_window(
    rank='rank(count)',
    sort=[alt.SortField('count', order='descending')]
).transform_filter(
    (alt.datum.rank <= 10)
).properties(width=700, height=300, title = "The 10 most frequent trigrams in the dataset").configure_title(
    fontSize=17,
    offset=25
).configure_axis(
    labelFontSize=13,
    titleFontSize=15,
    titlePadding=15
).configure_legend(
    gradientThickness=20,
    titleFontSize=15,
    labelFontSize=13,
    titlePadding=10
)

c
```

![tri_freq.png](attachment:tri_freq.png)

The word cloud is created:


```python
mask_tri=np.array(Image.open('grafici/number_three.jpg'))
at = ['#3C1067', '#075A23', '#44AA99', '#D55E00', '#AA4499', '#882255']
my_cmapt = ListedColormap(at)

wordcloud_tri = WordCloud(
            mask=mask_tri,
            width=mask_tri.shape[1],
            height=mask_tri.shape[0],
            background_color ='white', 
            min_word_length = 3,
            max_words=450,
            font_path = 'grafici/GothamMedium.ttf',
            min_font_size = 15,
            colormap=my_cmapt).generate_from_frequencies(tri)
```

Plot the word cloud:


```python
# Plot the word cloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_tri) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 
```

![cloud_tri_gen.png](attachment:cloud_tri_gen.png)
