from pandas.core.frame import DataFrame
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd
from scipy.stats.morestats import probplot


from statsmodels.formula.api import logit

import statsmodels.api as sm

def eachAllele(FileIn, Controles, FolderOut):
    CSV = pd.read_csv(FileIn)

    newColNames=['A_'+i.replace(':','_') for i in CSV.columns.values]


    CSV.columns = newColNames

    Controles = pd.read_csv(Controles)


    BothFrames = CSV.merge(Controles,left_on="A_IID", right_on="V1")

    print(BothFrames)

    keys = BothFrames.keys().to_list()


    keys = keys[2:len(keys)-2]

    if len(keys)>23:
        keys = keys[0:23]
    

    outFile = open(FolderOut+"/"+FileIn[FileIn.rfind('/')+1:], 'w')
    outFile.write("IID,Coefficient,StandardError,pValue")
    outFile.write('\n')


    for allele in keys:

        
        fit = logit("dx ~ {}+A_C1+A_C2".format(allele), BothFrames).fit()



        print(fit.summary())
        #pValue = 'NaN'
        
        pValue = fit.pvalues[1]

        print("pValue")
        print(pValue)
        


        coef = fit.params[len(fit.params)-3]
        print('coef')
        print(coef)

        stdErr = fit.bse[len(fit.bse)-3]
        print('STDErr')
        print(stdErr)


        IID = allele

        outFile.write(str(IID)+","+str(coef)+","+str(stdErr)+","+str(pValue)+'\n')
        #outFile.write(str(IID)+","+str(coef)+","+str(stdErr)+","+'\n')

        

def logitValues(FolderIn, FolderOut, Controles):
    os.makedirs(FolderOut)
    for path in os.listdir(FolderIn):
        #if (path != 'A.csv') and (path != 'B.csv') and (path != 'C.csv'):
        print(path)
        eachAllele(FolderIn+"/"+path,Controles,FolderOut)

       




logitValues("/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/SpecificControlCountwPlots", "/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/StatswPlotsP2", "/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/dxTable.csv")


#Run dif frames


# Read in and plot 
# One hot encoding
#     Store in a list
# Fitting Logit model 