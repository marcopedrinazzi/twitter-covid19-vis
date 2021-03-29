import csv
import pandas as pd
import json
pd.options.mode.chained_assignment = None

csv_dataframe = pd.read_csv('../dataset/fakecovid_filtered_dataset_clean_final.csv',sep=";")
csv_dataframe['tweet_id'] = csv_dataframe['tweet_id'].astype(str)

data = []
with open('../dataset/fakecovid_result_final_translated_full.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

#filtro gli ID in quanto il dataset contiene dei tweet non piu disponibili (circa 100)
index_id = 0
id_list = []
for element in data:
    id_list.append(data[index_id]['id_str'])
    index_id=index_id+1

boolean_series = csv_dataframe.tweet_id.isin(id_list)
filtered_df = csv_dataframe[boolean_series]
filtered_df.to_csv('FINAL_fakecovid_final_filtered_dataset_clean.csv',sep=';',index=False)

