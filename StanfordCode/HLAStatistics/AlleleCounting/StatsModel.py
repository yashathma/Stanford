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

# CSV = pd.read_csv("/Users/yash/Desktop/StanfordCode/HLAStatistics/CreatedFiles/CountingAlleleSpecific/A.csv")



# Controles = pd.read_csv("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv")

# Controles = Controles['dx'].tolist()

# CSV['Controles'] = Controles


# CSV.drop('ArrayID', inplace=True, axis=1)

# print(CSV)

# #fit = logit("Controles ~ A1", CSV).fit()

#print(fit.summary())

#print(CSV)


CSV = pd.read_csv("/Users/yash/Desktop/StanfordCode/HLAStatistics/CreatedFiles/CountingAlleleSpecific/A.csv")





newColNames=['A_'+i.replace(':','_') for i in CSV.columns.values]

print(newColNames)

CSV.columns = newColNames





print(CSV)

Controles = pd.read_csv("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv")




# Controles = Controles['dx'].tolist()

#CSV['Controles'] = Controles.dx.values

BothFrames = CSV.merge(Controles,left_on="A_IID", right_on="V1")





print(BothFrames.dx.value_counts())

fit = logit("dx ~ A_02_01", BothFrames).fit()

print(fit.params)
# print(fit.summary())





# print(CSV)
# print(CSV)






def EachAllele(CSVInPath, FolderPath, Allele1, Allele2, FileName):
    CSV = pd.read_csv(CSVInPath)

    A1 = CSV.loc[:,Allele1]
    A2 = CSV.loc[:,Allele2]

    A = pd.concat([A1,A2])

    keys = A.unique()

    keys = keys.tolist()


    keys.insert(0,'IID')


    Frame = DataFrame(data = CSV.loc[:,"IID"],columns=keys)

    Frame.set_index('IID')

    Frame.loc[:,Frame.keys()]=0

    Frame.loc[:,"IID"] = CSV.loc[:,"IID"]

    A1 = A1.to_list()
    A2 = A2.to_list()

    for i in range(0, len(A1)):
        if (A1[i]==A2[i]):
            Frame.loc[i,str(A1[i])]=2
        else:
            
            Frame.loc[i,str(A1[i])]=1
            Frame.loc[i,str(A2[i])]=1

    Frame.to_csv(FolderPath+"/"+FileName)


def CountingAllelesSpecific(CSVInPath, FolderPath):
    os.mkdir(FolderPath)

    CSV = pd.read_csv(CSVInPath)

    keys = CSV.keys().tolist()

    keys = keys[1:len(keys)-1]


    for i in range(0, len(keys)):
        if '.prob' not in str(keys[i]) and '.prob' not in str(keys[i+1]):
            EachAllele(CSVInPath,FolderPath, keys[i], keys[i+1], keys[i][0:len(keys[i])-2]+".csv")


#CountingAllelesSpecific("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv","/Users/yash/Desktop/StanfordCode/HLAStatistics/Test")


