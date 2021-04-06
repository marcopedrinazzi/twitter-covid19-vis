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

csv_dataframe = pd.read_csv('dataset/FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)
csv_list = csv_dataframe.values.tolist()
lista_unica_csv=list(itertools.chain.from_iterable(csv_list))

data = []
with open('dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
urls = []
titles = []
dates = []
category = []
for element in data:
    print(index)
    if data[index]['entities']['urls'] is not None:
        for entity in data[index]['entities']['urls']:
             #TIMEOUT
            #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

            # SERVONO DAVVERO SOLO QUESTI CAMPI?
            if entity['expanded_url'].lower() not in urls:
                token_id = data[index]['id_str']                          
                indice_csv = lista_unica_csv.index(token_id)   
                value_cat =  lista_unica_csv[indice_csv+1].lower()
                if value_cat == "false":
                    value_cat = "fake"
                try:
                    r = requests.get(entity['expanded_url'], timeout=10)
                except requests.exceptions.Timeout:
                    titles.append("[TIMEOUT ERROR]"+"("+entity['expanded_url'].lower()+")")
                    urls.append(entity['expanded_url'].lower())
                    category.append(value_cat.replace(" ", ""))
                    d = parse(data[index]['created_at'])
                    d = d.strftime('%Y/%m/%d')
                    dates.append(d)
                except requests.ConnectionError:
                    titles.append("[CONNECTION ERROR]"+"("+entity['expanded_url'].lower()+")")
                    urls.append(entity['expanded_url'].lower())
                    category.append(value_cat.replace(" ", ""))
                    d = parse(data[index]['created_at'])
                    d = d.strftime('%Y/%m/%d')
                    dates.append(d)
                else:
                    soup = BeautifulSoup(r.text,features="lxml")
                    if soup.title is None:
                        titles.append("[NO TITLE ERROR]"+"("+entity['expanded_url'].lower()+")")
                        urls.append(entity['expanded_url'].lower())
                        category.append(value_cat.replace(" ", ""))
                        d = parse(data[index]['created_at'])
                        d = d.strftime('%Y/%m/%d')
                        dates.append(d)
                    else:
                        titles.append("["+soup.title.text+"]"+"("+entity['expanded_url'].lower()+")")
                        urls.append(entity['expanded_url'].lower())
                        category.append(value_cat.replace(" ", ""))
                        d = parse(data[index]['created_at'])
                        d = d.strftime('%Y/%m/%d')
                        dates.append(d)
            else:
                print("URL già presente")
    index=index+1


df = pd.DataFrame(
    {'Type': category,
    'Link': titles,
    'First-Shared': dates
    })

df.to_csv('urls.csv', sep=',', index=False)