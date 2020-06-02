import torch
import torch.nn.functional as F
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from torch.nn.modules.distance import PairwiseDistance

def BERTembedding(sentence):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    input_ids = torch.tensor(tokenizer.encode(sentence,add_special_tokens=True)).unsqueeze(0)
    output = model(input_ids)
    last_hidden_states = output[0].squeeze(0)
    return last_hidden_states

class topKknowledge():
    def __init__(self, number, knowledge_max_len, compare_sentence, knowledges):
        self.number = number
        self.compare_sentence = compare_sentence
        self.t_knowledges = [knowledge['text'] for knowledge in knowledges]
        if len(compare_sentence) > knowledge_max_len:
            self.max_len = len(compare_sentence)
        else:
            self.max_len = knowledge_max_len

    def embedding(self):
        embedded_sentence = BERTembedding(self.compare_sentence)
        embedded_knowledges = torch.zeros([len(self.t_knowledges),self.max_len,768])
        for i in range(len(self._t_knowledge)):
            embedded_knowledges[i,:,:] = BERTembedding(self.t_knowledges[i])
        return embedded_sentence, embedded_knowledges

    def cosineSimilarity(self):
        cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
        top_k_knowledge = []
        for i,items in enumerate(self.t_knowledges):
            max_len = len(self.compare_sentence)
            output = cos(self.compare_sentence,self.knowledges[0])


    '''
    cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
    final_top_k = []
    for i,items in enumerate(zero_fact_list):
        lens = len(items)
        final = torch.zeros([lens,768])
        for j,item in enumerate(items):
            final[j,:] = cos(zero_question,item['bert'])
        scoring = F.softmax(final_mlp(final), dim=0)
        top_200 = torch.topk(torch.t(scoring),100)
        top_200_list = top_200[1].tolist()
        pre_top_fact = []
        #print('top :',top_200_list[0])
        for score in top_200_list[0]:
            pre_top_fact.append(fact_list[i][score])
            #print(fact_list[i][score])
        final_top_k.append(pre_top_fact)
    return final_top_k
    '''