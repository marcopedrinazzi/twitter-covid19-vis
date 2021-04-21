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

#Si chiama namer e poi si cancellano le entry inserite in urls_notitle_format.csv da urls_notitle.csv
df = pd.read_csv('urls_notitle.csv',sep=';')
l = df['Link'].to_list()

index=0
for u in l:
    try:
        print(str(index))
        print(u)
        r = requests.get(u, timeout=3) 
    except requests.exceptions.RequestException:
        print("ERRORE")
    else:
        soup = BeautifulSoup(r.text,'html.parser')
        if soup.title is None:
            print("NO TITLE")
        else:
            print(soup.title.text)
    print(" ")
    index=index+1

