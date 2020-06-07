import torch
import torch.nn.functional as F
import torch.nn as nn
from transformers import BertModel, BertTokenizer
from torch.nn.modules.distance import PairwiseDistance

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

class BERTembedding():
    def __init__(self):
        # load pretrained BERT model
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.model.to(device)

    def get_embedding(self, sentence):
        # make input token
        input_ids = torch.tensor(self.tokenizer.encode(sentence, add_special_tokens=True), device=device).unsqueeze(0).cuda()
        # result of embedding
        output = self.model(input_ids)
        last_hidden_states = output[0].squeeze(0)
        return last_hidden_states[1:-1]

class topKknowledge():
    def __init__(self, number, knowledge_max_len):
        self.number = number
        self.knowledge_max_len = knowledge_max_len
        self.embedder = BERTembedding()
        self.final_mlp = torch.nn.Sequential(
            torch.nn.Dropout(0.3, inplace=False),
            torch.nn.Linear(768, 512),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(0.3, inplace=False),
            torch.nn.Linear(512, 1),
        )

    def embedding(self, max_len, compare_sentence, t_knowledges):
        embedded_sentence = torch.zeros([max_len, 768],device=device)
        embedded_sentence[:len(compare_sentence),:] = self.embedder.get_embedding(compare_sentence)
        embedded_knowledges = torch.zeros([len(t_knowledges),max_len,768],device=device)
        for i in range(len(t_knowledges)):
            embedded_knowledges[i,:len(t_knowledges[i]),:] = self.embedder.get_embedding(t_knowledges[i])
        return embedded_sentence, embedded_knowledges

    def cosineSimilarity(self, embedded_sentence, embedded_knowledges):
        # set cosineSimilarity value
        cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)

        # set result tensor
        compare_result = torch.zeros([len(embedded_knowledges), 768])
        for i,embedded_knowledge in enumerate(embedded_knowledges):
            # output is result of cosineSimilarity(one knowledge)
            output = cos(embedded_sentence,embedded_knowledge)
            # compare_result is result of cosineSimilarity(all knowledges)
            compare_result[i,:] = self.final_mlp(output)
        return compare_result

    def get_topKknowledge(self, compare_sentence, knowledges, embedding_save=False):
        # text knowledges convert to list knowledges
        t_knowledges = [knowledge['text'].split(' ') for knowledge in knowledges]

        # set max_len
        if len(compare_sentence) > self.knowledge_max_len:
           max_len = len(compare_sentence)
        else:
           max_len = self.knowledge_max_len

        # 'embedded_sentence' is  compared sentence : [max_len, 768]
        # 'embedded_knowledges' is extracted knowledges :  [len(knowledges), max_len, 768]
        embedded_sentence, embedded_knowledges = self.embedding(max_len, compare_sentence, t_knowledges)

        # 'compare_result' is result of cosineSimilarity
        compare_result = self.cosineSimilarity(embedded_sentence, embedded_knowledges)

        # scoring
        scoring = F.softmax(compare_result, dim = 0)

        # extract top-K knowledges
        # top_K[0] : result of cosinesimilarity value
        # top_K[1] : result of cosinesimilarity index
        top_K = torch.topk(torch.t(scoring), self.number)
        top_K_list = top_K[1].tolist()

        # make result list
        if embedding_save:
            # embedding_save : True
            # result = [{'e1': str, 'rel': str, 'e2': str, 'text': str, 'embedding': tensor}, ...]
            result = []
            for i in top_K_list:
                pre_result = knowledges[i]
                pre_result['embedding'] = embedded_knowledges[i]
                result.append(pre_result)
        else:
            # embedding_save : False
            # result = [{'e1': str, 'rel': str, 'e2': str, 'text': str}, ...]
            result = [knowledges[i] for i in top_K_list]
        return result