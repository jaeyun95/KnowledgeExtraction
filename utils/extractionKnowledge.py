from pymongo import MongoClient
import random
import json

class extractionKnowledge():
    def __init__(self, number, max_len, version='mongo'):
        self.number = number
        self.max_len = max_len
        self.version = version
        if self.version == 'hash_table':
            self.hash_table = {}
            with open('generationDB/conceptnet/conceptnet.json', 'r', encoding="UTF8") as f:
                concept_list = [json.loads(s) for s in f]
            for i, concept in enumerate(concept_list):
                if concept['e1'] in self.hash_table.keys():
                    new = self.hash_table[concept['e1']] + [
                        {'e1': concept['e1'], 'rel': concept['rel'], 'e2': concept['e2'], 'text': concept['text'], '_id':concept['_id']}]
                    self.hash_table[concept['e1']] = new
                    continue
                self.hash_table[concept['e1']] = [
                    {'e1': concept['e1'], 'rel': concept['rel'], 'e2': concept['e2'], 'text': concept['text'], '_id':concept['_id']}]

    def _mongoDB(self, keywords):
        client = MongoClient('localhost', 27017)
        db = client.conceptnet
        collections = db.conceptnet5
        knowledges = []
        for i, keyword in enumerate(keywords):
            # cursor = collections.find({"$or":[{"e1":{"$regex":keyword}},{"e2":{"$regex":keyword}}]},no_cursor_timeout=True,limit=self.number)
            cursor1 = collections.find({"e1": {"$regex": keyword}}, no_cursor_timeout=True, limit=self.number)
            cursor2 = collections.find({"e2": {"$regex": keyword}}, no_cursor_timeout=True, limit=self.number)
            ex_results1 = list(cursor1)
            ex_results2 = list(cursor2)
            results = ex_results1 + ex_results2
            for result in results:
                text = result['text']
                if len(text.split(' ')) < self.max_len: knowledges.append(result)
        return knowledges

    def _hash_table(self, keywords):
        knowledges = []
        for i, keyword in enumerate(keywords):
            new_results = []
            if keyword[0] in self.hash_table.keys():
                results = self.hash_table[keyword[0]]
                random.shuffle(results)
                if self.number < len(results):
                    results = results[:100]
                    for result in results:
                        text = result['text']
                        if len(text.split(' ')) < self.max_len: new_results.append(result)
            knowledges += new_results
        return knowledges

    def get_knowledge(self, keywords):
        if self.version == 'mongo':
            return self._mongoDB(keywords)
        elif self.version == 'hash_table':
            return self._hash_table(keywords)
        else:
            raise ValueError("choice your version! mongo OR hash_table")