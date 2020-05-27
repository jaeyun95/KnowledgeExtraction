import torch
import torch.nn.functional as F
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from torch.nn.modules.distance import PairwiseDistance

def embedding(sentence):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    input_ids = torch.tensor(tokenizer.encode(sentence,add_special_tokens=True)).unsqueeze(0)
    output = model(input_ids)
    last_hidden_states = output[0].squeeze(0)
    return last_hidden_states

class topKknowledge():
    def __init__(self, number, compare_sentence, knowledges):
        self.number = number
        self.compare_sentence = compare_sentence
        self.t_knowledges = [knowledge['text'] for knowledge in knowledges]
        #self.output = torch

    def cosineSimilarity(self):
        cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
        output = cos(self.compare_sentence,self.knowledges[0])

    def euclideanSimilarity(selfs):
        euclidean = PairwiseDistance(2).forward(self.compare_sentence,self.t_knowledges)

    def manhattanSimilarity(self):

