#URL count
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
from collections import Counter
import requests
from bs4 import BeautifulSoup

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
urls = []
titles = []
for element in data:
    print(index)
    if data[index]['entities']['urls'] is not None:
        for entity in data[index]['entities']['urls']:
             #TIMEOUT
            #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

            # SERVONO DAVVERO SOLO QUESTI CAMPI?
            try:
                r = requests.get(entity['expanded_url'], timeout=10)
            except requests.exceptions.Timeout:
                titles.append("TIMEOUT ERROR")
                urls.append(entity['expanded_url'])
            except requests.ConnectionError:
                titles.append("CONNECTION ERROR")
                urls.append(entity['expanded_url'])
            else:
                soup = BeautifulSoup(r.text,features="lxml")
                if soup.title is None:
                    titles.append("NO TITLE ERROR")
                    urls.append(entity['expanded_url'])
                else:
                    titles.append(soup.title.text)
                    urls.append(entity['expanded_url'])
        
    index=index+1


df = pd.DataFrame(
    {'Title': titles,
    'Urls': urls
    })

df.to_csv('urls.csv', sep=',', index=False)