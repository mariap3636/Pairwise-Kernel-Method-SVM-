#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.

from sklearn.metrics import roc_curve, auc, precision_recall_curve, precision_recall_fscore_support

def AUROC(correct_label, predict_score):
  fpr, tpr, _ = roc_curve(correct_label, predict_score)
  auroc = auc(fpr, tpr)
  return auroc

def AUPR(correct_label, predict_score):
  precision, recall, _ = precision_recall_curve(correct_label, predict_score)
  aupr = auc(recall, precision)
  return aupr
