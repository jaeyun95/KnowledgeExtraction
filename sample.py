from dataloaders.vcr import VCR
from utils.extractionKeyword import extractionKeyword
from utils.extractionKnowledge import extractionKnowledge
from utils.topKknowledge import topKknowledge
import time # this is test
import torch


# definee keyword extractor
keywordExtractor = extractionKeyword()

# define knowledge extractor
knowledgeExtractor = extractionKnowledge(5,10)

# define topK extractor
topKExtractor = topKknowledge(50,10)

## set your sentence
sentence = "doc is cute and cat is cute too."

## extract keyword from your sentence(tokenized)
tokenized_sentence = sentence.split(' ')

## extract keyword
keywords = knowledgeExtractor.get_keyword(tokenized_sentence)

## extract knowledges
knowledges = knowledgeExtractor.extract(keywords, sentence)

## extract topK knowledges
topKknowledge = knowledgeExtractor._extract_topK(sentence, knowledges)