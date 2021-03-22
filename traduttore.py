##############
##########
#######
##
#traduttore
##
#######
##########
##############

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
    for entity in data[index]['entities']['hashtags']:
        entity['text']=translator.translate(entity['text'],lang_tgt='en')
    index=index+1


with open('fakecovid_result_translated.json', 'a') as f:
    for line in data:
        json.dump(line, f)
        f.write('\n')

f.close()