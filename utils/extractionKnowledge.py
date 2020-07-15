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
            #cursor = collections.find({"$or":[{"e1":{"$regex":keyword}},{"e2":{"$regex":keyword}}]},no_cursor_timeout=True,limit=self.number)
            cursor1 = collections.find({"e1": {"$regex": keyword}},no_cursor_timeout=True, limit=self.number)
            cursor2 = collections.find({"e2": {"$regex": keyword}}, no_cursor_timeout=True, limit=self.number)
            ex_results1 = list(cursor1)
            ex_results2 = list(cursor2)
            results = ex_results1 + ex_results2
            for result in results:
                text = result['text']
                if len(text.split(' ')) < self.max_len: knowledges.append(result)
        return knowledges