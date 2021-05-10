import json
import pandas as pd
import csv
import itertools
import demoji
from collections import Counter
import nltk
import altair as alt
from nltk.corpus import stopwords
import re
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
import string
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder,TrigramCollocationFinder, TrigramAssocMeasures
from operator import itemgetter
import contractions
import num2words
alt.data_transformers.disable_max_rows()

#csv_dataframe = pd.read_csv('twitter-covid19-vis/fakecovid/dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
#csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
#csv_list = csv_dataframe.values.tolist()
#lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

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
with open('twitter-covid19-vis/fakecovid/dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

data1 = []
with open('general_result_translated_full.json', 'r') as f1:
    for line in f1:
        data1.append(json.loads(line))

index=0
stop_words = stopwords.words('english')
new_bigram=[]
for element in data:
    data[index]['full_text'] = data[index]['full_text'].lower()                      # Put everything in lowercase
    data[index]['full_text'] = contractions.fix(data[index]['full_text'])
    #data[index]['full_text'] = re.sub("\'\w+", '', data[index]['full_text'])        # Remove everything after '
    data[index]['full_text'] = remove_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_twitter_urls(data[index]['full_text'])
    data[index]['full_text'] = remove_emoticons(data[index]['full_text'])
    data[index]['full_text'] = remove_emoji(data[index]['full_text'])
    data[index]['full_text'] = give_emoji_free_text(data[index]['full_text'])
    data[index]['full_text'] = noamp(data[index]['full_text'])                        # No amp with space
    data[index]['full_text'] = re.sub("#\S+", " ",  data[index]['full_text'])         # Remove hashtags
    data[index]['full_text'] = re.sub("@\S+", " ",  data[index]['full_text'])         # No mentions
    data[index]['full_text'] = data[index]['full_text'].translate(str.maketrans('', '', string.punctuation)) # No puntuaction
    data[index]['full_text'] = data[index]['full_text'].encode('ascii', 'ignore').decode() # No unicode
    data[index]['full_text'] = re.sub("^rt ", " ", data[index]['full_text'])          # No RT
    data[index]['full_text'] = re.sub('\s{2,}', " ", data[index]['full_text'])        # Remove big spaces
    bigram_tokens=list(nltk.bigrams(nltk.word_tokenize(data[index]['full_text'])))
    #print(bigram_tokens)
    clean_bigram_tokens = [gram for gram in bigram_tokens if not any(stop in gram for stop in stop_words)]
    for c in clean_bigram_tokens:
        final_token = ' '.join(c) + " " +"fakecovid"
        #print(final_token)
        new_bigram.append(final_token)
    #new_bigram.append(clean_bigram_tokens)
    index=index+1

index_tri=0
stop_words_tri = stopwords.words('english')
new_bigrama=[]
for element in data1:
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].lower()                # Put everything in lowercase
    data1[index_tri]['full_text'] = contractions.fix(data1[index_tri]['full_text'])
    #data[index_tri]['full_text'] = re.sub("\'\w+", '', data[index_tri]['full_text'])  # Remove everything after '
    data1[index_tri]['full_text'] = remove_urls(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_twitter_urls(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_emoticons(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = remove_emoji(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = give_emoji_free_text(data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = noamp(data1[index_tri]['full_text'])                 # No amp with space
    data1[index_tri]['full_text'] = re.sub("#\S+", " ",  data1[index_tri]['full_text'])  # Remove hashtags
    data1[index_tri]['full_text'] = re.sub("@\S+", " ",  data1[index_tri]['full_text'])  # No mentions
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].translate(str.maketrans('', '', string.punctuation)) # No puntuaction
    data1[index_tri]['full_text'] = data1[index_tri]['full_text'].encode('ascii', 'ignore').decode() # No unicode
    data1[index_tri]['full_text'] = re.sub("^rt ", " ", data1[index_tri]['full_text'])   # No RT
    data1[index_tri]['full_text'] = re.sub(r'\b\d\b', lambda x: num2words.num2words(int(x.group(0))), data1[index_tri]['full_text'])
    data1[index_tri]['full_text'] = re.sub('\s{2,}', " ", data1[index_tri]['full_text']) # Remove big spaces
    trigram_tokens=list(nltk.bigrams(nltk.word_tokenize(data1[index_tri]['full_text'])))
    #print(trigram_tokens)
    clean_trigram_tokens = [gram for gram in trigram_tokens if not any(stop in gram for stop in stop_words_tri)]
    for c in clean_trigram_tokens:
        final_token = ' '.join(c) + " " +"generalcovid"
        #print(final_token)
        new_bigrama.append(final_token)
    index_tri=index_tri+1

merged_final = new_bigram + new_bigrama

c = dict(nltk.FreqDist(merged_final))

df = pd.DataFrame.from_dict(c, orient='index').reset_index()
df = df.rename(columns={'index':'Bigram', 0:'Count'})

col_one_list = df['Bigram'].tolist()
col_two_list = df['Count'].tolist()

count_general= [0] * len(col_one_list)
count_fake = [0] * len(col_one_list)

namelist = []
index = 0

for el in col_one_list:
    tok = el.split()
    a = tok[0] + " " + tok[1]
    namelist.append(a)
    indx = namelist.index(a)
    if tok[2] == "generalcovid":
        count_general[indx] = col_two_list[index]
    elif tok[2] == "fakecovid":
        count_fake[indx] = col_two_list[index]
    else:
        print("errore count")
    index = index + 1

df['Bigram']=namelist
df['General Covid']=count_fake
df['Fake Covid']=count_general
del df['Count']

df_norm = df.copy()
df_norm[['General Covid', 'Fake Covid']] = (df_norm[['General Covid', 'Fake Covid']] - df_norm[['General Covid', 'Fake Covid']].min()) / (df_norm[['General Covid', 'Fake Covid']].max() - df_norm[['General Covid', 'Fake Covid']].min())
#print(df_norm.to_string())

#a = df_norm.to_json(orient='records')
#print(a)

a = alt.Chart(df_norm).mark_text().encode(
    x=alt.X('General Covid', scale=alt.Scale(type="log")),
    y=alt.Y('Fake Covid', scale=alt.Scale(type="log")), #, scale=alt.Scale(type="log")
    #color=alt.Color('Words',legend=None),
    #text="Hashtag",
#   tooltip=['Mentions', 'General Covid', 'Fake Covid']
).transform_filter(
    {"and": [alt.FieldGTPredicate(field='General Covid', gt=0), alt.FieldGTPredicate(field='Fake Covid', gt=0)]}
).properties(width=800,height=500)

#text = a.mark_text(
#    align='left',
#    baseline='middle',
#    dx=7
#).encode(
#    text='Hashtag'
#)

#(a+text).show()

a.show()