import os
import numpy as np
import torch
import nltk

class extractionKeyword():
    def __init__(self, instance):
        self.question = instance['question']
        self.answer_list = instance['answer_list']
        #self.visual_concepts = instance['visual_concpets']

    def _remove_stopword(self):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        stop_words.update(['.','\'s','\'',',','?','why','how','what','where','when','yes','no'])
        self.question = [w.lower() for w in self.question if w.lower() not in stop_words]
        self.question = list(set(self.question))
        for i,answer in enumerate(self.answer_list):
            self.answer_list[i] = [w.lower() for w in answer if w.lower() not in stop_words]
            self.answer_list[i] = list(set(self.answer_list[i]))

    def _prototype(self):
        lm = nltk.stem.WordNetLemmatizer()
        self.question = [lm.lemmatize(w, pos="v") for w in self.question]
        for i,answer in enumerate(self.answer_list):
            self.answer_list[i] = [lm.lemmatize(w, pos="v") for w in answer]

    def get_keyword(self):
        self._remove_stopword()
        self._prototype()
        return self.question, self.answer_list