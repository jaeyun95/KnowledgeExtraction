import csv
from pymongo import MongoClient
import re
client = MongoClient('localhost',27017)
db = client.conceptnet
collections = db.conceptnet5

with open('assertions.csv','r',encoding="UTF8") as f:
    items = csv.reader(f)
    for i,item in enumerate(items):
        list_to_string = ''.join(item)
        re_split = list_to_string.split('\t')
        relation=re_split[1].split('/')[-1]
        check1, start = re_split[2].split('/')[2:4]
        check2, end = re_split[3].split('/')[2:4]
        start = re.sub('[^a-zA-Z]', ' ', start).lstrip()
        end = re.sub('[^a-zA-Z]', ' ', end).lstrip()
        if start == '' or end == '': continue
        if check1 == 'en' and check2 == 'en':
            pre_node = {}
            pre_node['e1'] = start
            pre_node['rel'] = relation
            pre_node['e2'] = end
            if relation == 'RelatedTo':
                sentence = start + ' is related to ' + end
            elif relation == 'FormOf':
                sentence = start + ' is the root word of ' + end
            elif relation == 'IsA':
                sentence = start + ' is ' + end
            elif relation == 'PartOf':
                sentence = start + ' is part of ' + end
            elif relation == 'HasA':
                sentence = start + ' has ' + end
            elif relation == 'UsedFor':
                sentence = start + ' is used for ' + end
            elif relation == 'CapableOf':
                sentence = start + ' can ' + end
            elif relation == 'AtLocation':
                sentence = start + ' can be at ' + end
            elif relation == 'Causes':
                sentence = start + ' causes you to ' + end
            elif relation == 'HasSubevent':
                sentence = 'Something you might do while ' + start + ' is ' + end
            elif relation == 'HasFirstSubevent':
                sentence = 'The first thing you do when you ' + start + ' is ' + end
            elif relation == 'HasLastSubevent':
                sentence = 'The last thing you do when you ' + start + ' is ' + end
            elif relation == 'MannerOf':
                sentence = start + ' is a way to ' + end
            elif relation == 'SimilarTo':
                sentence = start + ' is similar to ' + end
            elif relation == 'EtymologicallyRelatedTo':
                sentence = start + ' and ' + end +' have a common origin'
            elif relation == 'CausesDesire':
                sentence = start + ' would make you want to ' + end
            elif relation == 'MadeOf':
                sentence = start + ' is made of ' + end
            elif relation == 'HasPrerequisite':
                sentence = 'Something you need to do before you ' + start + ' is ' + end
            elif relation == 'HasProperty':
                sentence = 'Something you need to do before you ' + start + ' is ' + end
            elif relation == 'MotivatedByGoal':
                sentence = 'You would ' + start + ' because you want ' + end
            elif relation == 'ObstructedBy':
                sentence = start + ' is a goal that can be prevented by  ' + end
            elif relation == 'Desires':
                sentence = start + ' wants to ' + end
            elif relation == 'CreatedBy':
                sentence = start + ' is created by ' + end
            elif relation == 'Synonym':
                sentence = start + ' is a translation of ' + end
            elif relation == 'Antonym':
                sentence = start + ' is the opposite of ' + end
            elif relation == 'DistinctFrom':
                sentence = start + ' is not ' + end
            elif relation == 'DerivedFrom':
                sentence = start + ' and ' + end + ' are distinct member of a set'
            elif relation == 'SymbolOf':
                sentence = start + ' symbolically represents ' + end
            elif relation == 'DefinedAs':
                sentence = start + ' is the ' + end
            elif relation == 'LocatedNear':
                sentence = start + ' is typically near ' + end
            elif relation == 'HasContext':
                sentence = start + ' is a word used in the context of ' + end
            elif relation == 'EtymologicallyDerivedFrom':
                sentence = start + ' is derived from ' + end
            elif relation == 'ReceivesAction':
                sentence = start + ' can be ' + end
            pre_node['text'] = sentence
            print(pre_node)
            #collections.insert(pre_node)