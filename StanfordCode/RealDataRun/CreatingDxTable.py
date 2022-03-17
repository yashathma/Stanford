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


df = pd.read_csv("/Users/yash/Desktop/StanfordCode/RunningData/FormatedData.csv")

df = df[['IID','DX']]
df = df.rename(columns={"DX": "dx", "IID": "V1"})

df.to_csv('/Users/yash/Desktop/StanfordCode/RunningData/dxTable.csv')
