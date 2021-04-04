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
for element in data:
    print("indice "+str(index))
    print(data[index]['entities']['urls'])
    if data[index]['entities']['urls'] is not None:
        for entity in data[index]['entities']['urls']:
            r = requests.get(entity['expanded_url'], timeout=10)
            #TIMEOUT
            #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
            soup = BeautifulSoup(r.text,features="lxml")
            if soup.title is None:
                urls.append("none " + entity['expanded_url'])
            else:
                urls.append(soup.title.text + " " + entity['expanded_url'])
        
    index=index+1

print(urls)