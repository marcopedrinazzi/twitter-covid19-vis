import gzip
import shutil
import os
import wget
import csv
import linecache
from shutil import copyfile
import ipywidgets as widgets
import numpy as np
import pandas as pd

filtered_language = "en"
#NOTABENE
#Il nome del file full_dataset.tsv va cambiato con il nome del dataset

#If language specified, it will create another tsv file with the filtered records
filtered_tw = list()
current_line = 1
with open("full_dataset_clean.tsv") as tsvfile:
  tsvreader = csv.reader(tsvfile, delimiter="\t")

  if current_line == 1:
    filtered_tw.append(linecache.getline("full_dataset_clean.tsv", current_line))

    for line in tsvreader:
      if line[3] == filtered_language:
        filtered_tw.append(linecache.getline("full_dataset_clean.tsv", current_line))
      current_line += 1

  print('\033[1mShowing first 5 tweets from the filtered dataset\033[0m')
  print(filtered_tw[1:(6 if len(filtered_tw) > 6 else len(filtered_tw))])

  with open('clean-dataset-filtered.tsv', 'w') as f_output:
      for item in filtered_tw:
          f_output.write(item)

 