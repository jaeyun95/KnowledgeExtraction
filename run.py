from dataloaders.vcr import VCR
from extractionKeyword import extractionKeyword
from extractionKnowledge import extractionKnowledge
from topKknowledge import topKknowledge
import time
import torch


train_answer = VCR('train','answer')
train_rationale = VCR('train','rationale')
#val_answer = VCR('val','answer')
#val_rationale = VCR('val', 'rationale')
#test_answer = VCR('test','answer')
#test_rationale = VCR('test', 'rationale')

keywordExtractor = extractionKeyword()
knowledgeExtractor = extractionKnowledge(50,10)
topKExtractor = topKknowledge(50,10)

print('start!!!')
start = time.time()
for t_answer,t_rationale in zip(train_answer,train_rationale):
    answer_list = []
    rationale_list = []
    for i in range(4):
        answer_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_answer['answer_list'][i])))
        #rationale_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_rationale['answer_list'][i])))
        topKExtractor.get_topKknowledge(t_answer['question'],answer_list[i])
        #topKExtractor.get_topKknowledge(t_rationale['question'], rationale_list[i])
end = time.time()
print('time : ',end-start)
