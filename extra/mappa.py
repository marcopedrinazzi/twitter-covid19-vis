import pandas as pd
import numpy as np
import json
import sys
import string
import re
from collections import Counter
import altair as alt
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import plotly.express as px

data = []
with open('general_result_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

index=0
lati = []
longi = []
texto = []
both = []
counter = []
locator = Nominatim(user_agent="myGeocoder")
for element in data: 
    print(index)
    if data[index]['place'] is not None:#se c'è coordinates c'è anche place
        location = locator.geocode(data[index]['place']['full_name'])
        if location is not None:
            #long.append(location.longitude)
            #lat.append(location.latitude)
            both.append(str(location.longitude)+" "+str(location.latitude) + " "+location.address.replace(" ","."))
            #text.append(location.address)
    index=index+1

c = Counter(both)
df = pd.DataFrame.from_dict(c, orient='index').reset_index()
df = df.rename(columns={'index':'address', 0:'count'})
print(df.to_string())
add = df['address'].to_list()
co = df['count'].to_list()
i = 0
for a in add:
    s = a.split()
    longi.append(s[0])
    lati.append(s[1])
    texto.append(s[2].replace("."," "))
    counter.append(co[i])
    i = i + 1


#print(c)

dfnew = pd.DataFrame(
    {'Long': longi,
     'Lat': lati,
     'Text':texto,
     'Count':counter,
    })

#indirizzo = dfnew['Text'].to_list()
#country = []
#for i in indirizzo:
#   country.append(i.split(",")[-1])


#dfnew['Continent'] = continente
#print(dfnew.to_string())
dfnew.to_csv("grafico2.csv", index=False)

