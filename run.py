#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.

import convertfile as cf
import cross_validation as cv
import evaluate as ev
from pkm import PairwiseKernelMethod

Kp = cf.readMat("dataset/protein/GPCR.txt")
Kc = cf.readMat("dataset/compound/GPCR.txt")
correctLabel = cf.readMat("dataset/interaction/GPCR.txt")
LabelP, LabelC = cf.readAxisLabel("dataset/interaction/GPCR.txt")

pkm = PairwiseKernelMethod(Kp, Kc, correctLabel, LabelP, LabelC)
cv_set = cv.Kfold_interaction(correctLabel, 10)
ave = 0
for i, (train, test) in enumerate(cv_set):
    auroc = ev.AUROC(correctLabel.ravel()[test], pkm.run(train, test)[:,1])
    ave += auroc
    print(auroc)
print("average:" + str(ave/10))
