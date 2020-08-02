import csv
from pymongo import MongoClient
from pymongo import TEXT
import re
import json
import time # this is test

hash_table = {}
fact_dict = {}
with open('conceptnet5_small_version.json','r',encoding="UTF8") as f:
    concept_list = [json.loads(s) for s in f]

for i, concept in enumerate(concept_list):
    print(i)
    if concept['e1'] in hash_table.keys():
        new = hash_table[concept['e1']] + [{'e1':concept['e1'],'rel':concept['rel'],'e2':concept['e2'],'text':concept['text']}]
        hash_table[concept['e1']] = new
        continue
    hash_table[concept['e1']] = [{'e1':concept['e1'],'rel':concept['rel'],'e2':concept['e2'],'text':concept['text']}]




