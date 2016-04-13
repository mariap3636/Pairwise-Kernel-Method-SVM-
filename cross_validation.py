#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Faburary 19, 2016.
import numpy as np
from sklearn.cross_validation import StratifiedKFold
import random

#make protein-wise cross validation dataset
def Kfold_protein(interaction, n_folds):
    ret = []
    t_len, c_len = interaction.shape
    dataset = np.asarray(range(t_len*c_len))
    for i in xrange(n_folds):
        samp = random.sample(range(t_len), t_len/n_folds)
        samp.sort()
        test = []
        for j in samp:
            test.extend(np.where((dataset>=j*c_len)&(dataset<(j+1)*c_len))[0].tolist())
        train = list(set(range(len(dataset))) - set(test))
        train.sort()
        ret.append((np.asarray(train),np.asarray(test)))
    return ret

#make compound-wise cross validation dataset
def Kfold_compound(interaction, n_folds):
    ret = []
    t_len, c_len = interaction.shape
    dataset = np.asarray(range(t_len*c_len))
    for i in xrange(n_folds):
        samp = random.sample(range(c_len), c_len/n_folds)
        samp.sort()
        test = []
        for j in samp:
            test.extend(np.where(dataset%c_len == j)[0].tolist())
        test.sort()
        train = list(set(range(len(dataset))) - set(test))
        train.sort()
        ret.append((np.asarray(train),np.asarray(test)))
    return ret

#make interaction-wise cross validation dataset
def Kfold_interaction(interaction, n_folds):
    dataset = interaction.ravel()
    return StratifiedKFold(dataset, n_folds = n_folds, shuffle = True)
