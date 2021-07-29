from pandas.core.frame import DataFrame
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd


CSV = pd.read_csv("/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv")

A1 = CSV.loc[:,"A.1"]
A2 = CSV.loc[:,"A.1"]


A1 = A1.to_list()
A2 = A2.to_list()

# print(A1)
# print(A2)

['02:01', '03:01', '24:02', '11:01', '01:01', '02:06', '25:01', '02:07', '33:03', '23:01', '31:01', '26:01', '02:11', '30:01', '02:05', '29:02', '68:02', '30:02', '32:01', '29:01', '02:02', '11:02', '24:03', '33:01', '34:01', '34:02', '01:02', '30:04', '66:01', '74:01', '68:01', '36:01', '69:01', '68:17', '66:02', '80:01']



MainList = []

for i in range(0,len(A1)):
    if A1[i] not in MainList:
        MainList.append(A1[i])
    
    if A2[i] not in MainList:
        MainList.append(A2[i])

print(MainList)