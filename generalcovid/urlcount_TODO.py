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
import datetime
from dateutil.parser import parse
import csv
import itertools

data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
urls = []
titles = []
dates = []
for element in data:
    print(index)
    if data[index]['entities']['urls'] is not None:
        for entity in data[index]['entities']['urls']:
            print(entity['expanded_url'])
            if entity['expanded_url'].lower() not in urls:
                try:
                    r = requests.get(entity['expanded_url'], timeout=10)
                except requests.exceptions.Timeout:
                    titles.append("[TIMEOUT ERROR]"+"("+entity['expanded_url'].lower()+")")
                    urls.append(entity['expanded_url'].lower())
                    d = parse(data[index]['created_at'])
                    d = d.strftime('%Y/%m/%d')
                    dates.append(d)
                except requests.ConnectionError:
                    titles.append("[CONNECTION ERROR]"+"("+entity['expanded_url'].lower()+")")
                    urls.append(entity['expanded_url'].lower())
                    d = parse(data[index]['created_at'])
                    d = d.strftime('%Y/%m/%d')
                    dates.append(d)
                else:
                    soup = BeautifulSoup(r.text,features="lxml")
                    if soup.title is None:
                        titles.append("[NO TITLE ERROR]"+"("+entity['expanded_url'].lower()+")")
                        urls.append(entity['expanded_url'].lower())
                        d = parse(data[index]['created_at'])
                        d = d.strftime('%Y/%m/%d')
                        dates.append(d)
                    else:
                        titles.append("["+soup.title.text+"]"+"("+entity['expanded_url'].lower()+")")
                        urls.append(entity['expanded_url'].lower())
                        d = parse(data[index]['created_at'])
                        d = d.strftime('%Y/%m/%d')
                        dates.append(d)
            else:
                print("URL già presente")
    index=index+1


df = pd.DataFrame(
    {'Link': titles,
    'First-Shared': dates
    })

df.to_csv('urls_g.csv', sep=',', index=False)