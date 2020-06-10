import torch
import torch.nn.functional as F
import torch.nn as nn
import  h5py

class VCRSaver():
    def __init__(self, path, file_name, number, embedding=False):
        self.path = path
        self.file_name = file_name
        self.saver = h5py.File(f'{self.path}_{self.file_name}','w')
        self.number = number
        self.embedding = embedding

    def save(self, answer_results, rationale_results):
        print('=====================================start!======================================')
        # make h5 group
        for i in range(self.number):
            self.saver.create_group(f'{i}')
            group = self.saver[f'{i}']
            for k in range(4):
                group.create_dataset(f'answer_{i}', data=answer_results[k][i])
                group.create_dataset(f'rationale_{i}', data=rationale_results[k][i])

        print('file path : ',self.path)
        print('file name : ',self.file_name)
        print('=====================================finish!=====================================')

