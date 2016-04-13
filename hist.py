#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.

import convertfile as cf
import link_indicator as li
import itertools
import matplotlib.pyplot as plt

CPI = cf.readMat("dataset/interaction/ionchannel.txt")
LabelP, LabelC = cf.readAxisLabel("dataset/interaction/ionchannel.txt")
p_comb = list(itertools.combinations_with_replacement(LabelP,2))

CPI_network = li.mat2Network(CPI, LabelP, LabelC, range(len(LabelC)*len(LabelP)))
indicator = li.preds2Mat(li.cosine_similarity(CPI_network, p_comb), LabelP).ravel()
one = np.asarray(np.where(indicator==1)[0])

# G = li.GIP(CPI).ravel()

plt.hist(indicator, bins=20, color="green", range=(0.0,1.0))
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.ylim(0, 40000)
plt.show()
