from dataloaders.vcr import VCR

instance = VCR('val', 'rationale')

for i,item in enumerate(instance):
    print(item)