#!/usr/bin/env python
#
# Copywrite (c) 2016 Takuro Yamazaki.
#
# Last update: Febrary 19, 2016.
import numpy as np

def readMat(filepath):
    f = open(filepath)
    y_size = len(f.readline().split("\t"))
    extract = range(1,y_size + 1)
    Imat = [map(float, np.asarray(f.readline().split("\t"))[extract])]
    line = f.readline()
    while line:
        row = [map(float, np.asarray(line.split("\t"))[extract])]
        Imat = np.concatenate((Imat,row))
        line = f.readline()
    f.close()
    return np.asarray(Imat)

def readAxisLabel(filepath):
    f = open(filepath)
    x_lst = []
    y_lst = f.readline().split("\t")
    line = f.readline()
    while line:
        x_lst.append(line.split("\t")[0])
        line = f.readline()
    f.close()
    return (x_lst, y_lst)
