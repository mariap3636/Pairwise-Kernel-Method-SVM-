#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy import stats, spatial

"""
#calvulate user similarity with peason correlation
def PearsonSim(self):
    usrln = len(self.user_list)
    ret = np.zeros((usrln, usrln))
    for i in xrange(usrln):
        if(i <= j):
            for j in xrange(usrln):
                tmp = stats.pearsonr(user_item_relation[i], user_item_relation[j])
                ret[i][j] = tmp
                ret[j][i] = tmp
    return ret

#calvulate user similarity with cosine similarity
def CosineSim(self):
    usrln = len(self.user_list)
    ret = np.zeros((usrln, usrln))
    for i in xrange(usrln):
        if(i <= j):
            for j in xrange(usrln):
                tmp = 1 - spatial.distance.cosine(user_item_relation[i], user_item_relation[j])
                ret[i][j] = tmp
                ret[j][i] = tmp
    return ret


#calculate predict score using user based CF
def UserBasedCF(self):
    usrln = len(self.user_list)
    itmln = len(self.item_list)
    colmn_ave = np.sum(self.user_item_matrix, axis=1)/itmln
    ret = np.zeros((usrln, itmln))
    for i in xrange(usrln):
        for j in xrange(itmln):
            ret = self.user_item_matrix[i][j] - colmn_ave[i]
    denominator_lst = np.sum(self.user_similarity, axis=1)
    numerator_mat = np.dot(self.user_similarity, self.ret)
    for i in xrange(usrln):
        denomi = denominator_lst[i]
        if(denomi != 0):
            for j in xrange(itmln):
                ret[i][j] = colmn_ave[i] + numerator_mat[i][j]/denomi
    return ret
"""

def read_mat(filepath):
    rating_mat = lil_matrix((USERS, PRODUCTS))
    f = open(filepath, 'r')
    for line in f:
        line = line.rstrip()
        yid, pid, rate = line.split(' ')
        rating_mat[int(yid),int(pid)] = int(rate)
    return rating_mat


def PearsonSim(sparse_mat, obj_usr):
    sparse_mat = sparse_mat.tocsr()
    uu_sim = np.zeros(USERS)
    for user in xrange(USERS):
        uu_sim[user] = stats.pearsonr(sparse_mat.getrow(obj_usr), sparse_mat.getrow(user))
    sparse_mat = sparse_mat.tolil()
    return uu_sim


#上の指標にはcsrを渡す
def NaiveCF(sparse_mat):
    colmn_ave = sparse_mat.mean(axis=1)
    

