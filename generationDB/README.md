## This is generate Knowledge DataBase using ConceptNet

This is for knowledge extraction from knowlede databse(conceptnet).
ConcentNet have many knowledge, so retrieval time is too long.
ConcentNet have many Language(maybe 304) But i use only english.
So, i edit conceptnet and save MongoDB.

# 1.Download Knowledge json file
You download ConcentNet json file first. Link is [Here](https://github.com/commonsense/conceptnet5/wiki/Downloads)

# 2.Install MongoDB(Ubuntu 16.04)
You install MongoDB in your environment.
MongoDB install instruction like this:
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64,arm64,ppc64el,s390x ] http://repo.mongodb.com/apt/ubuntu xenial/mongodb-enterprise/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise.list
sudo apt-get update
sudo apt-get install -y mongodb-org

#start server
sudo service mongod start
```

# 3.Run conceptnet.py
You run conceptnet.py file. This is save english knowledge into MongoDB.
I convert conceptnet relation to text like below.
### Relation and Text Table
|**Relation**|**Text**|**Relation**|**Text**|
|------|------|------|------|
|RelatedTo|is related to|HasPrerequisite|Something you need to do before you A is B|
|FormOf|is the root word of|HasProperty|Something you need to do before you  A is B|
|IsA|is|MotivatedByGoal|You would A because you want B|
|Part of|is part of|ObstructedBy|is a goal that can be prevented by|
|HasA|has|Desires|wants to|
|UsedFor|is used for|CreatedBy|is created by|
|CapableOf|can|Synonym|is a translation of|
|AtLocation|can be at|Antonym|is the opposite of|
|Causes|causes you to|DistinctFrom|is not|
|HasSubevent|Something you might do while A is B|DerivedFrom|A and B are distinct member of a set|
|HasFirstSubevent|The first thing you do when you A is B|SymbolOf|symbolically represents|
|HasLastSubevent|The last thing you do when you A is B|DefinedAs|is the|
|MannerOf|is a way to|LocatedNear|is typically near|
|SimilarTo|is similar to|HasContext|is a word used in the context of|
|EtymologicallyRelatedTo|A and B have a common origin|EtymologicallyDerivedFrom|is derived from|
|CausesDesire|would make you want to|ReceivesAction|can be|
|MadeOf|is made of|||

### Run
```
python conceptnet.py

#knowledge example
{ "_id" : ObjectId("5ec624c4ae42e4918a908948"), "e1" : "abapical", "rel" : "Antonym", "e2" : "apical", "text" : "abapical is the opposite of apical" }
```

# 4.Make conceptnet.json file(export conceptnet.json from MongoDB)
This is your choice. I use json file because, mongoDB is too slow.(if you extract little knowledge, i recommand using MongoDB)
```
mongoexport -d DATABASE_NAME -c COLLECTION_NAME -o FILENAME.json --port 27017
```
