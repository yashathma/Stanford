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

def formatingCSV(path):
    df = path
    df = df.drop(columns=['C1', 'C2', 'V5', 'V6', 'V7', 'V8', 'DX2'])
    return df

def creatingDXTable(CSVIn):
    df = CSVIn[['IID','DX']]
    return df.rename(columns={"DX": "dx", "IID": "V1"})

def EachAllele(CSVIn, C1, C2, Allele1, Allele2, FileName):
    CSV = CSVIn

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


    Frame['C1'] = C1
    Frame['C2'] = C2
    return (Frame)

def CountingAllelesSpecific(CSVIn, C1, C2):
    CSV = CSVIn

    keys = CSV.keys().tolist()
    

    keys = keys[1:len(keys)-1]

    finalList = []

    for i in range(0, len(keys)):
        if '.prob' not in str(keys[i]) and '.prob' not in str(keys[i+1]):
            finalList.append(EachAllele(CSVIn, C1, C2, keys[i], keys[i+1], keys[i][0:len(keys[i])-2]+".csv"))

    return finalList, keys

def eachAllele(FileIn, Controles, FolderOut, key):
    CSV = FileIn

    newColNames=['A_'+i.replace(':','_') for i in CSV.columns.values]

    CSV.columns = newColNames


    BothFrames = CSV.merge(Controles,left_on="A_IID", right_on="V1")
    print(BothFrames)


    keys = BothFrames.keys().to_list()


    keys = keys[2:len(keys)-2]

    if len(keys)>12:
        keys = keys[0:12]

    outFile = open(FolderOut+"/"+key+'.csv', 'w')
    outFile.write("IID,Coefficient,StandardError,pValue")
    outFile.write('\n')



    # print('Before')
    # print(BothFrames.dtypes)
    # #BothFrames = BothFrames.dtypes.astype(int, True, errors = 'raise')
    # for i in range(0,len(BothFrames.dtypes)):
    #     BothFrames.dtypes[i] = 'int'
    #     #print(BothFrames.dtypes[i])

    # print('After')
    # print(BothFrames.dtypes)

    for column in BothFrames.columns:
        BothFrames[column].astype(int)

    # print(BothFrames.rows)
    # print(BothFrames.rows.astype(int))





    for allele in keys:
        print("allele")
        print(allele)
        fit = logit("dx ~ {}+A_C1+A_C2".format(allele), BothFrames).fit()

        print(fit.summary())
        
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

def formatkeys(keys):
    listkeys = []
    for i in range(0,len(keys),3):
        listkeys.append(keys[i][0:keys[i].index('.')])
    return listkeys

def logitValues(FolderIn, FolderOut, Controles, keys):
    os.makedirs(FolderOut)
    for i in range(0,len(FolderIn)):
        eachAllele(FolderIn[i],Controles,FolderOut, keys[i])


CSVIn = pd.read_csv("/Users/yash/Desktop/StanfordCode/RunningData/DX_HLA_CALLS_noIDS/TrueData.csv")

C1 = CSVIn['C1']
C2 = CSVIn['C2']

CSVIn = formatingCSV(CSVIn)

dxtable = creatingDXTable(CSVIn)

CountingAlleleControles, keys = CountingAllelesSpecific(CSVIn, C1, C2)

keys = formatkeys(keys)

logitValues(CountingAlleleControles,"/Users/yash/Desktop/StanfordCode/RunningData/NextDataSet/RunTest", dxtable, keys)