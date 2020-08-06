import torch
import torch.nn.functional as F
import torch.nn as nn
from pymongo import MongoClient
from .topKknowledge import BERTembedding
import json
import h5py

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

class saveModule():
    def __init__(self, knowledges, version='version'):
        self.version = version
        self.knowledges = knowledges

    def save(self):
        if self.version == 'mongo':
            self.mongo()
        elif self.version == 'json':
            self.json()
        elif self.version == 'h5':
            self.h5()
        else:
            raise ValueError("choice your version! mongo OR json OR h5")

    def mongo(self):
        client = MongoClient('localhost', 27017)
        db = client.result
        collections = db.knowledges
        data = {'knowledges':self.knowledges}
        collections.insert(data)
        print('mongo version saving success!')

    def json(self):
        json_file = ""
        for i, item in enumerate(self.knowledges):
            jstring = json.dumps(item)
            json_file += jstring + '\n'
        f = open('knowledges.json', "w")
        f.write(json_file)
        f.close()
        print('json version saving success!')

    def h5(self):
        output = h5py.File(f'knowledges.h5', 'w')
        embedder = BERTembedding()
        for i, knowledge in enumerate(self.knowledges):
            print(i)
            output.create_group(f'{i}')
            embedded_knowledge = embedder.get_embedding(knowledge['text'].split(' '))
            output[f'{i}'].create_dataset(f'knowledge', data=embedded_knowledge.cpu().detach().numpy())
        print('h5 version saving success!')

