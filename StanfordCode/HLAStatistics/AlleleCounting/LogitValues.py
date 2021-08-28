from numpy.core.fromnumeric import std
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



def getCoefSTD(filePath, controlesPath):
    CSV = pd.read_csv(filePath)

    newColNames=['A_'+i.replace(':','_') for i in CSV.columns.values]



    CSV.columns = newColNames


    Controles = pd.read_csv(controlesPath)


    BothFrames = CSV.merge(Controles,left_on="A_IID", right_on="V1")

    # print(CSV)
    # print(list(CSV)[2])

    fit = logit("dx ~ "+list(CSV)[2], BothFrames).fit()



    return fit.params[1], fit.bse[1]


    


def coefSTD(folderPath, newFilePath, controlesPath):
    #os.mkdir(newFolderPath)

    data = []
    Columns = ['IID','Coefficient','Standard Error']

    for path in os.listdir(folderPath):
        coef, STD = getCoefSTD(folderPath+"/"+path, controlesPath)
        data.append([path[0:path.index('.')],coef,STD])


    df = pd.DataFrame(data, columns = Columns)


    
    df.to_csv(newFilePath)
        
    



coefSTD("/Users/yash/Desktop/StanfordCode/HLAStatistics/CreatedFiles/CountingAlleleSpecific", "/Users/yash/Desktop/StanfordCode/HLAStatistics/CoefSTD.csv","/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv")