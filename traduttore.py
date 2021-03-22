######
####
##
#
#traduttore
######
####
##
#

import json
import sys
import string
from google_trans_new import google_translator  


data = []
with open('fakecovid_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

f.close()


index=0
translator = google_translator()  
for element in data:
    data[index]['full_text']=translator.translate(data[index]['full_text'],lang_tgt='en')
    index=index+1

#to do
with open('newfakecovid_result.json', 'w') as f:
    json.dump(data,f)

f.close()
