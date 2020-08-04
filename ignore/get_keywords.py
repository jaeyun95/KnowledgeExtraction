from dataloaders.vcr import VCR
from utils.extractionKeyword import extractionKeyword
from utils.extractionKnowledge import extractionKnowledge
from utils.topKknowledge import topKknowledge
import time # this is test
import torch
import json

train_answer = VCR('train','answer')
train_rationale = VCR('train','rationale')
val_answer = VCR('val','answer')
val_rationale = VCR('val', 'rationale')
test_answer = VCR('test','answer')
test_rationale = VCR('test', 'rationale')

# definee keyword extractor
keywordExtractor = extractionKeyword()

k = 0
keyword_list = []
for t_answer,t_rationale in zip(train_answer,train_rationale):
    for i in range(4):
        keyword_list += keywordExtractor.get_keyword(t_answer['answer_list'][i])
        keyword_list += keywordExtractor.get_keyword(t_rationale['answer_list'][i])
    keyword_list += t_rationale['objects']
    keyword_list = list(set(keyword_list))
    print('train : ',k)
    k += 1

k = 0
for v_answer,v_rationale in zip(val_answer,val_rationale):
    for i in range(4):
        keyword_list += keywordExtractor.get_keyword(v_answer['answer_list'][i])
        keyword_list += keywordExtractor.get_keyword(v_rationale['answer_list'][i])
    keyword_list += v_rationale['objects']
    keyword_list = list(set(keyword_list))
    print('val : ', k)
    k += 1

k = 0
for test_answer,test_rationale in zip(test_answer,test_rationale):
    for i in range(4):
        keyword_list += keywordExtractor.get_keyword(test_answer['answer_list'][i])
        keyword_list += keywordExtractor.get_keyword(test_rationale['answer_list'][i])
    keyword_list += test_rationale['objects']
    keyword_list = list(set(keyword_list))
    print('test : ',k)
    k += 1

print('finish! len is ',len(keyword_list))

keyword_dict = [{'keyword':keyword_list}]
print(keyword_dict)
before_json = ""
for i,item in enumerate(keyword_dict):
    jstring = json.dumps(item)
    before_json += jstring + '\n'


f = open('keyword.json',"w")
f.write(before_json)
f.close()