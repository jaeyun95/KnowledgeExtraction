import os
import numpy as np
import torch
import nltk

class extractionKeyword():
    def __init__(self, instance):
        self.question = instance['question']
        self.answer_list = instance['answer_list']
        #self.visual_concepts = instance['visual_concpets']

    def _prototype(self):
