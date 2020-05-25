from dataloaders.vcr import VCR
from extractionKeyword import extractionKeyword

instance = VCR('val', 'rationale')

for i,item in enumerate(instance):
    keyword = extractionKeyword(item)
    question, answer_list = keyword.get_keyword()
    print(question)
