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
        #output_h5_2 = h5py.File(f'extract_feature/vcr_new_tag_image_train.h5', 'w')
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
        '''
        output_h5.create_group(f'{image_id}')
        group2use = output_h5[f'{image_id}']
        group2use.create_dataset(f'image_id', data=image_id)
        group2use.create_dataset(f'image_h', data=image_h)
        group2use.create_dataset(f'image_w', data=image_w)
        group2use.create_dataset(f'features', data=final_features)
        group2use.create_dataset(f'boxes', data=final_boxes)
        group2use.create_dataset(f'num_boxes', data=final_boxes.shape[0])
        '''

