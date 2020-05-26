from dataloaders.vcr import VCR
from extractionKeyword import extractionKeyword
from extractionKnowledge import extractionKnowledge

train_answer = VCR('train','answer')
train_rationale = VCR('train','rationale')
#val_answer = VCR('val','answer')
#val_rationale = VCR('val', 'rationale')

keywordExtractor = extractionKeyword()
knowledgeExtractor = extractionKnowledge(50,10)

for t_answer,t_rationale in zip(train_answer,train_rationale):
    print(keywordExtractor.get_keyword(t_answer['question']))

