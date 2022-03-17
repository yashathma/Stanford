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

#Format and getting df

df = pd.read_csv("/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/TrueData.csv")


C1 = df['C1']
C2 = df['C2']

df = df.drop(columns=['C1', 'C2', 'V5', 'V6', 'V7', 'V8', 'DX2'])

countingfiles = []

for filename in os.listdir('/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/SpecificControlCount'):
    countingfiles.append((filename))





for path in countingfiles:
    df = pd.read_csv('/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/SpecificControlCount/'+path)
    df['C1'] = C1
    df['C2'] = C2
    df.to_csv("/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/SpecificControlCountwPlots/"+path)

    





#print(countingfiles)

