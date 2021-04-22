#Domain count
import pandas as pd
import numpy as np
import json
import sys
import string
from collections import Counter
import csv
import itertools
from urllib.parse import urlparse

data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
domains = []
for element in data:
    #print(index)
    if data[index]['entities']['urls'] is not None:
        for entity in data[index]['entities']['urls']:
            domain = urlparse(entity['expanded_url'].lower()).netloc
            if domain!="twitter.com":
                domains.append("["+domain+"]"+"("+domain+")")
    
    #print(" ")
    index=index+1

count = Counter(domains)
df = pd.DataFrame.from_dict(count, orient='index').reset_index()
df = df.rename(columns={'index':'domain', 0:'count'})
df = df.sort_values(by=['count'], ascending=False)
#print(df.to_string())

df.to_csv('domains_general.csv', sep=';', index=False)