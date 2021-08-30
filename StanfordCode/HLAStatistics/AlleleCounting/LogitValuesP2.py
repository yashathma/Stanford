from pandas.core.frame import DataFrame
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd


from statsmodels.formula.api import logit

import statsmodels.api as sm

def eachAllele(FileIn, Controles, FolderOut):
    CSV = pd.read_csv(FileIn)

    newColNames=['A_'+i.replace(':','_') for i in CSV.columns.values]


    CSV.columns = newColNames

    Controles = pd.read_csv(Controles)


    BothFrames = CSV.merge(Controles,left_on="A_IID", right_on="V1")

    keys = BothFrames.keys().to_list()


    keys = keys[2:len(keys)-2]

    if len(keys)>23:
        keys = keys[0:23]
    

    outFile = open(FolderOut+"/"+FileIn[FileIn.rfind('/')+1:], 'w')
    outFile.write("IID,Coefficient,StandardError")
    outFile.write('\n')

    #x = 0

    for allele in keys:
        
        fit = logit("dx ~ "+allele, BothFrames).fit()

        #print(fit.summary())
        #print(fit.llr)
        

        coef = fit.params[1]
        stdErr = fit.bse[1]
        IID = allele

        outFile.write(str(IID)+","+str(coef)+","+str(stdErr)+'\n')
        #x+=1
        #print(x)
        

def logitValues(FolderIn, FolderOut, Controles):
    os.makedirs(FolderOut)
    for path in os.listdir(FolderIn):
        print(path)
        eachAllele(FolderIn+"/"+path,Controles,FolderOut)




logitValues("/Users/yash/Desktop/StanfordCode/HLAStatistics/CreatedFiles/CountingAlleleSpecific", "/Users/yash/Desktop/StanfordCode/HLAStatistics/Test", "/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv")
