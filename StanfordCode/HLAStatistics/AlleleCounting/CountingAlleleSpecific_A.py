from pandas.core.frame import DataFrame
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd


def CountingAllelesSpecific(CSVInPath, CSVOutPath):
    CSV = pd.read_csv(CSVInPath)

    Frame = DataFrame(data = CSV.loc[:,"IID"],columns=['IID','02:01', '03:01', '24:02', '11:01', '01:01', '02:06', '25:01', '02:07', '33:03', '23:01', '31:01', '26:01', '02:11', '30:01', '02:05', '29:02', '68:02', '30:02', '32:01', '29:01', '02:02', '11:02', '24:03', '33:01', '34:01', '34:02', '01:02', '30:04', '66:01', '74:01', '68:01', '36:01', '69:01', '68:17', '66:02', '80:01'])
    Frame.set_index('IID')

    Frame.loc[:,Frame.keys()]=0
    
    Frame.loc[:,"IID"] = CSV.loc[:,"IID"]


    A1 = CSV.loc[:,"A.1"]
    A2 = CSV.loc[:,"A.2"]

    A1 = A1.to_list()
    A2 = A2.to_list()

    for i in range(0, len(A1)):
        if (A1[i]==A2[i]):
            Frame.loc[i,str(A1[i])]=2
        else:
            
            Frame.loc[i,str(A1[i])]=1
            Frame.loc[i,str(A2[i])]=1

    Frame.to_csv(CSVOutPath)





CountingAllelesSpecific("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv","/Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleCountingSpecific_A.csv")