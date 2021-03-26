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
#from googletrans import Translator
#from deep_translator import GoogleTranslator

data = []
with open('general_result_translated_textonly.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

f.close()


index=0
#translator_altro = Translator()
translator = google_translator()  
for element in data:
    if data[index]['lang']=="en":
        print(str(index)+" già inglese")
    else:
        #translated  = translator.translate(data[index]['full_text'],lang_tgt='en')  
        #data[index]['full_text'] = translated
        #time.sleep(1)
        #print(str(index)+" indice" + data[index]['full_text'])
        for entity in data[index]['entities']['hashtags']:
            translated = translator.translate(entity['text'],lang_tgt='en')#lang_tgt è l'alt
            entity['text']=translated
            time.sleep(1)
            print(str(index)+" indice" + entity['text'])
    index=index+1


with open('general_result_translated_full.json', 'a') as f_w:
    for line_w in data:
        print("sto stampando")
        json.dump(line_w, f_w)
        f_w.write('\n')

f.close()