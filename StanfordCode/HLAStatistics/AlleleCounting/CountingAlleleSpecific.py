from pandas.core.frame import DataFrame
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd


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


#CountingAllelesSpecific("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv","/Users/yash/Desktop/StanfordCode/HLAStatistics/CountingAlleleSpecific", 'B.1', 'B.2', "A.csv")

CountingAllelesSpecific("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv","/Users/yash/Desktop/StanfordCode/HLAStatistics/Test")