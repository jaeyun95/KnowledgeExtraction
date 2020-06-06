import torch
import torch.nn.functional as F
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from torch.nn.modules.distance import PairwiseDistance

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

def BERTembedding(sentence):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    model.to(device)
    input_ids = torch.tensor(tokenizer.encode(sentence,add_special_tokens=True),device=device).unsqueeze(0).cuda()
    output = model(input_ids)
    last_hidden_states = output[0].squeeze(0)
    return last_hidden_states[1:-1]

class topKknowledge():
    def __init__(self, number, knowledge_max_len):
        self.number = number
        self.knowledge_max_len = knowledge_max_len
        #self.compare_sentence = compare_sentence
        #self.t_knowledges = [knowledge['text'] for knowledge in knowledges]
        #if len(compare_sentence) > knowledge_max_len:
        #    self.max_len = len(compare_sentence)
        #else:
        #    self.max_len = knowledge_max_len

        self.final_mlp = torch.nn.Sequential(
            torch.nn.Dropout(0.3, inplace=False),
            torch.nn.Linear(768, 512),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(0.3, inplace=False),
            torch.nn.Linear(512, 1),
        )

    def embedding(self, max_len, compare_sentence, t_knowledges):
        embedded_sentence = torch.zeros([max_len, 768],device=device)
        embedded_sentence[:len(compare_sentence),:] = BERTembedding(compare_sentence)
        embedded_knowledges = torch.zeros([len(t_knowledges),max_len,768],device=device)
        for i in range(len(t_knowledges)):
            embedded_knowledges[i,:len(t_knowledges[i]),:] = BERTembedding(t_knowledges[i])
        return embedded_sentence, embedded_knowledges

    def cosineSimilarity(self, embedded_sentence, embedded_knowledges):
        cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
        top_k_knowledge = []
        for i,items in enumerate(self.t_knowledges):
            output = cos(self.compare_sentence,self.knowledges[0])
            top_k_knowledge.append(self.final_mlp(output))
        return top_k_knowledge

    def get_topKknowledge(self, compare_sentence, knowledges):
        t_knowledges = [knowledge['text'].split(' ') for knowledge in knowledges]
        if len(compare_sentence) > self.knowledge_max_len:
           max_len = len(compare_sentence)
        else:
           max_len = self.knowledge_max_len
        embedded_sentence, embedded_knowledges = self.embedding(max_len, compare_sentence, t_knowledges)
        print(embedded_sentence)

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