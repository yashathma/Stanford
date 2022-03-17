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

df = pd.read_csv("/Users/yash/Desktop/StanfordCode/RunningData/TrueData.csv")

df = df.drop(columns=['C1', 'C2', 'V5', 'V6', 'V7', 'V8', 'DX2'])

df.to_csv("/Users/yash/Desktop/StanfordCode/RunningData/FormatedData.csv")

print(df)