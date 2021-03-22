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
import time
from googletrans import Translator


data = []
with open('fakecovid_result.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

f.close()


index=0
translator_altro = Translator(service_urls=['translate.googleapis.com'])
translator = google_translator()  
for element in data:
    data[index]['full_text']=translator_altro.translate(data[index]['full_text'],dest='en')
    print("sleep dopo full_text")
    time.sleep(5)
    for entity in data[index]['entities']['hashtags']:
        entity['text']=translator_altro.translate(entity['text'],dest='en')#lang_tgt è l'alt
        print("sleep dopo hashtag")
        time.sleep(5)
    index=index+1


with open('fakecovid_result_translated.json', 'a') as f:
    for line in data:
        json.dump(line, f)
        f.write('\n')

f.close()