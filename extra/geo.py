import pandas as pd
import numpy as np
import json
import sys
import string
import re
from collections import Counter
import altair as alt

data = []
with open('dataset/general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
new = []
for element in data: 
    if data[index]['place'] is not None:
        token=data[index]['place']['name']
        new.append(token)
    index=index+1

print(len(new))
count=Counter(new)
#print(count)
