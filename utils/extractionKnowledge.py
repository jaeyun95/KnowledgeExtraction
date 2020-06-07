from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.conceptnet
collections = db.conceptnet5

class extractionKnowledge():
    def __init__(self, number, max_len):
        self.number = number
        self.max_len = max_len

    def get_knowledge(self, keywords):
        knowledges = []
        for i, keyword in enumerate(keywords):
            cursor = collections.find({"$or":[{"e1":{"$regex":keyword}},{"e2":{"$regex":keyword}}]},no_cursor_timeout=True,limit=self.number)
            results = list(cursor)
            for result in results:
                text = result['text']
                if len(text.split(' ')) < self.max_len: knowledges.append(result)
        return knowledges