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
with open('fakecovid_result_translated_text_only.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

f.close()


index=0
#translator_altro = Translator()
translator = google_translator()  
for element in data:
    #translated_full = translator.translate(data[index]['full_text'],lang_tgt='en')
    #data[index]['full_text']=translated_full
    #time.sleep(1)
    print(str(index)+" indice")
    for entity in data[index]['entities']['hashtags']:
        translated = translator.translate(entity['text'],lang_tgt='en')#lang_tgt è l'alt
        entity['text']=translated
        time.sleep(1)
        print("sleep dopo hashtag")
    index=index+1


with open('fakecovid_result_translated_full.json', 'a') as f_w:
    for line_w in data:
        print(line)
        json.dump(line_w, f_w)
        f_w.write('\n')

f.close()