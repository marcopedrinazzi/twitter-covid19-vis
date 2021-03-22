import pandas as pd
import numpy as np
import json
import sys
import string
import re
import collections

data = []
with open('general_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
new = []
for element in data:
    new.append(data[index]["lang"])
    index=index+1

print(len(new))
print(collections.Counter(new))

