import numpy as np
import math

def easyInput(num):
    if(num == 1):
        print("this is enzyme")
        return "enzyme"
    if(num == 2):
        print("this is ionchannel")
        return "ionchannel"
    if(num == 3):
        print("this is GPCR")
        return "GPCR"
    if(num == 4):
        print("this is NuclearRecepter")
        return "NuclearRecepter"

def matShape(name):
    if(name == "enzyme"):
        return (664, 445)
    if(name == "NuclearRecepter"):
        return (26, 54)
    if(name == "ionchannel"):
        return (204, 210)
    if(name == "GPCR"):
        return (95, 223)

def readInteractiondata(name):
    N = matShape(name)[0]
    M = matShape(name)[1]
    f = open('./dataset/drug-target instruction/' + name + '.txt')
    x_lst = []
    line = f.readline()
    y_lst = line.split("\t")
    GMAT = np.zeros((N,M))
    line = f.readline()
    j = 0
    one = 0
    while line:
        x = line.split("\t")
        x_lst.append(x[0])
        n_lst = range(1, len(x))
        #make edge from side ef to drug
        for i in n_lst:
            if(x[i].strip() == "1"):
                GMAT[j][i-1] = 1
                one += 1
        j += 1
        line = f.readline()
    print("one is " + str(one))
    f.close()
    return (N, M, x_lst, y_lst, GMAT)

def readCompoundSim(name):
    M = matShape(name)[1]
    f = open('./dataset/Compound Simirality/' + name + '.txt')
    line = f.readline()
    SIM = np.zeros((M,M))
    j = 0
    line = f.readline()
    while line:
        x = line.split("\t")
        n_lst = range(1, len(x))
        #make edge from side ef to drug
        for i in n_lst:
            SIM[j][i-1] = float(x[i].strip())
        j += 1
        line = f.readline()
    f.close()
    return SIM

def readProteinSim(name):
    N = matShape(name)[0]
    f = open('./dataset/Protein Simirality/' + name + '.txt')
    line = f.readline()
    SIM = np.zeros((N,N))
    j = 0
    line = f.readline()
    while line:
        x = line.split("\t")
        n_lst = range(1, len(x))
        #make edge from side ef to drug
        for i in n_lst:
            SIM[j][i-1] = float(x[i].strip())
        j += 1
        line = f.readline()
    f.close()
    return SIM
