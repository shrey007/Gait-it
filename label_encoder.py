'''
    Utility module to get labels
'''

import os

def getLabels(path):
  '''
        Parameters:
        path (string): path to files in google drive

        Returns:
        labels_to_idx (dictionary): labels to index
        idx_to_label (dictionary): index to labels
    '''
  files = os.listdir(path )
  labels = set()
    
  for f in files:
    label = f.partition('_')[0]
    labels.add(label)
    
  labels_to_idx = {label:idx for idx, label in enumerate(labels)}
  idx_to_labels = {idx:label for idx, label in enumerate(labels)}
    
  return labels_to_idx, idx_to_labels