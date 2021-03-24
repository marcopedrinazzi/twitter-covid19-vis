import pandas as pd
import numpy as np
import json
import sys
import string
import re
import itertools  
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emoji
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import nltk
from PIL import Image
import altair as alt
import csv

csv_dataframe = pd.read_csv('fakecovid_dataset_clean.csv',sep=";")
#print(csv_dataframe)

csv_list = csv_dataframe.values.tolist()
print(len(csv_list))

data = []
with open('fakecovid_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
#comment_words = ''
cmt_list = []
stopwords = set(STOPWORDS) 
for element in data:
    id = data[index]['id']
    #print("index: "+str(index)+" tweet id: " + str(id))
    id_list = csv_list[index][0]
    #print("index: "+str(index)+" id list: " + str(id_list))
    token=data[index]['user']['screen_name']
    cmt_list.append(token)
    #comment_words += token + " "
    index=index+1

