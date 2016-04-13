#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.
from __future__ import division
import networkx as nx
import math
import itertools
from sklearn.metrics.pairwise import rbf_kernel
import numpy as np
from scipy import stats

def GIP(mat):
    return rbf_kernel(mat, mat, gamma=1)

def Zscore(mat):
    M,N = mat.shape
    zscore = stats.zscore(mat.ravel())
    RET = zscore.reshape((M,N))
    return RET

def mat2Network(mat, xlbl, ylbl, train):
    vec = mat.ravel()
    comblbl = list(itertools.product(xlbl, ylbl))
    G = nx.Graph()
    G.add_nodes_from(xlbl)
    G.add_nodes_from(ylbl)
    for element in train:
        if(vec[element] == 1):
            G.add_edge(comblbl[element][0], comblbl[element][1])
    return G

def preds2Mat(preds, lbl):
    leng = len(lbl)
    RET = np.zeros((leng, leng))
    for u,v,p in preds:
        RET[lbl.index(u)][lbl.index(v)] = p
        RET[lbl.index(v)][lbl.index(u)] = p
    return RET

#ebunch is list of node pair
def jaccard_coefficient(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        union_size = len(set(G[u]) | set(G[v]))
        if union_size == 0:
            return 0
        else:
            return len(cnbors) / union_size
    return ((u, v, predict(u, v)) for u, v in ebunch)

def adamic_adar_index(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        return sum(1 / math.log(G.degree(w))
                   for w in nx.common_neighbors(G, u, v))
    return ((u, v, predict(u, v)) for u, v in ebunch)

def resource_allocation_index(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        sum_cn = 0
        for w in cnbors:
            if not G.degree(w) == 0:
                #print("debug")
                sum_cn += 1/math.fabs(G.degree(w))
        return sum_cn
    return ((u, v, predict(u, v)) for u, v in ebunch)

def preferential_attachment(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    return ((u, v, G.degree(u) * G.degree(v)) for u, v in ebunch)

def common_neighbor(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        return len(cnbors)
    return ((u, v, predict(u, v)) for u, v in ebunch)

def cosine_similarity(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        cosine_val = math.sqrt(G.degree(u) * G.degree(v))
        if cosine_val == 0:
            return 0
        else:
            return len(cnbors) / cosine_val
    return ((u, v, predict(u, v)) for u, v in ebunch)

def hpi(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        min_val = min(G.degree(u), G.degree(v))
        if min_val == 0:
            return 0
        else:
            return len(cnbors) / min_val
    return ((u, v, predict(u, v)) for u, v in ebunch)

def hdi(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        max_val = max(G.degree(u), G.degree(v))
        if max_val == 0:
            return 0
        else:
            return len(cnbors) / max_val
    return ((u, v, predict(u, v)) for u, v in ebunch)

def lhn(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors = list(nx.common_neighbors(G, u, v))
        mult_val = G.degree(u) * G.degree(v)
        if mult_val == 0:
            return 0
        else:
            return len(cnbors)/ mult_val
    return ((u, v, predict(u, v)) for u, v in ebunch)

def sorensen(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        cnbors_len = len(list(nx.common_neighbors(G, u, v)))
        denomi = G.degree(u) + G.degree(v)
        if denomi == 0:
            return 0
        else:
            return (2*cnbors_len) / denomi
    return ((u, v, predict(u, v)) for u, v in ebunch)

def graph_distance(G, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(G)
    def predict(u, v):
        if(nx.has_path(G, u, v)):
            s_path_length = nx.shortest_path_length(G, source = u, target = v)
            return (-1) * s_path_length
        else:
            return -100
    return ((u, v, predict(u, v)) for u, v in ebunch)
