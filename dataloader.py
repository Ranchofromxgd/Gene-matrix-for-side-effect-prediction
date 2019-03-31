import torch
from torchvision.datasets import ImageFolder
import torch
from torchvision import transforms
from torch.utils.data import DataLoader

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pickle


row = 100
col = 80
assert row*col >= 8000

class matLoader(torch.utils.data.Dataset):
    def __init__(self,training_scale):
        print('Loading files...')
        self.training_scale = training_scale
        self.mono = pd.read_csv('bio-decagon-mono/bio-decagon-mono.csv')
        self.combo = pd.read_csv('bio-decagon-combo/bio-decagon-combo.csv')
        self.effectcategories = pd.read_csv('bio-decagon-effectcategories/bio-decagon-effectcategories.csv')
        self.targets = pd.read_csv('bio-decagon-targets/bio-decagon-targets-all.csv')
        self.ppi = pd.read_csv('bio-decagon-ppi/bio-decagon-ppi.csv')
        self.se = self.combo['Polypharmacy Side Effect'].tolist()

        f = open('./pickles/gene2id.pkl','rb')
        f1 = open('./pickles/id2gene.pkl','rb')
        f2 = open('./pickles/se2id.pkl','rb')
        f3 = open('./pickles/id2se.pkl','rb')
        print("Current workpath:"+os.getcwd())
        self.gene2id = pickle.load(f)
        self.id2gene = pickle.load(f1)
        self.se2id = pickle.load(f2)
        self.id2se = pickle.load(f3)
        f.close()
        f1.close
        f2.close()
        f3.close()

        self.id2coo = {}
        self.count = 0
        for i in range(0,row):
            for j in range(0,col):
                self.id2coo[self.count] = [i,j]
                self.count+=1

    def get_stitch_gene(self,index):
        st1 = self.combo[index:index+1]['STITCH 1'].tolist()[0]
        st2 = self.combo[index:index+1]['STITCH 2'].tolist()[0]
        gene1 = self.targets[self.targets['STITCH'] == st1]['Gene'].tolist()
        gene2 = self.targets[self.targets['STITCH'] == st2]['Gene'].tolist()
        for i in range(0,len(gene1)):
            gene1[i] = self.gene2id[gene1[i]]
        for i in range(0,len(gene2)):
            gene2[i] = self.gene2id[gene2[i]]
        return gene1,gene2

    def stat2mat(self,lis1,lis2):
        mat1 = np.zeros((row,col))
        mat2 = np.zeros((row,col))
        for each in lis1:
            mat1[self.id2coo[each][0],self.id2coo[each][1]] += 1
        for each in lis2:
            mat2[self.id2coo[each][0],self.id2coo[each][1]] += 1
        #return np.hstack((mat1,mat2))
        return mat1+mat2

    def __getitem__(self,index):
        side_effect = self.combo[index:index+1]['Polypharmacy Side Effect'].tolist()[0]
        gene1,gene2 = self.get_stitch_gene(index)
        se_mat = torch.zeros(1,row,col)
        se_mat[0,:,:] = torch.Tensor(self.stat2mat(gene1,gene2))
        return se_mat,self.se2id[side_effect]
    def __len__(self):
        return self.training_scale

if __name__ == '__main__':
    training_scale = 1000
    dataloader = matLoader(training_scale)

    cnt = 0
    for each in dataloader:
        print(each)
        cnt+=1
        if(cnt == 3):
            break
