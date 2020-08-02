import csv
from pymongo import MongoClient
from pymongo import TEXT
import re
import json
client = MongoClient('localhost',27017)
db = client.conceptnet5_example
collections = db.conceptnet5_index

collections.create_index([('e1',TEXT)], default_language='english')

with open('conceptnet5_small_version.json','r',encoding="UTF8") as f:
    concept_list = [json.loads(s) for s in f]

for concept in concept_list:
    del concept['_id']
    collections.insert(concept)
