## This is generate Knowledge DataBase using ConceptNet

This is for knowledge extraction from knowlede databse(conceptnet).
ConcentNet have many knowledge, so retrieval time is so long.
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
```
python conceptnet.py

#knowledge example
{ "_id" : ObjectId("5ec624c4ae42e4918a908948"), "e1" : "abapical", "rel" : "Antonym", "e2" : "apical", "text" : "abapical is the opposite of apical" }
```