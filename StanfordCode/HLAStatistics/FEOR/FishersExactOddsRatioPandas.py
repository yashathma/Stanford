from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os
import pandas as pd



#python3 /Users/yash/Desktop/StanfordCode/HLAStatistics/FEOR/FishersExactOddsRatioPandas.py -CSVInPath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv -ControlTablePath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv -OutFolderPath /Users/yash/Desktop/StanfordCode/HLAStatistics/CSVInFishersOdds

def AlleleFishersExactOddsRatio(CSVInPath, ControlTablePath, OutFolderPath, FileName, A1, A2):
    
    
    Controls = []
    Cases = []

    NewControls = []
    NewCases = []

    dx = pd.read_csv(ControlTablePath)

    CSVIN = pd.read_csv(CSVInPath)

    dxCon = dx.loc[dx['dx'] == 1]
    Controls = dxCon['V1'].to_list()

    dxCas = dx.loc[dx['dx'] == 0]
    Cases = dxCas['V1'].to_list()


    Keys = CSVIN.keys()
    IID = Keys[0]
    A1 = Keys[A1]
    A2 = Keys[A2]

    IID = CSVIN[IID].to_list()
    CSVINA1 = CSVIN[A1].to_list()
    CSVINA2 = CSVIN[A2].to_list()








    for i in range(0,len(CSVIN)):
        if(Controls.count(IID[i])>0):
            NewControls.append(CSVINA1[i])
            NewControls.append(CSVINA2[i])
        else:
            NewCases.append(CSVINA1[i])
            NewCases.append(CSVINA2[i])




    controlsCount = Counter(NewControls)

    notControlsCount = Counter(NewCases)

    keys = list(controlsCount.keys())

    outFile = open(OutFolderPath+'/'+FileName, 'w')

    outFile.write(','.join(['Allele','Control', 'ControlFrequency', 'Case', 'CaseFrequency','Pvalue','OddsRatio']))
    outFile.write('\n')
    
    for n in range(0,len(keys)-1):
        oddsRatio, pValue = fisher_exact([[notControlsCount[keys[n]],3000-notControlsCount[keys[n]]],[controlsCount[keys[n]],1000-controlsCount[keys[n]]]])
        outFile.write(str(keys[n])+','+str(controlsCount[keys[n]])+','+ str((controlsCount[keys[n]])/(len(Controls+Cases)*2)) +','+str(notControlsCount[keys[n]])+','+ str((notControlsCount[keys[n]])/(len(Controls+Cases)*2))+','+str(pValue)+','+str(oddsRatio)+'\n')


def FishersExactOddsRatio(CSVInPath, ControlTablePath, OutFolderPath):
    os.makedirs(OutFolderPath)

    with open(CSVInPath) as hlaFile:
        for n, line in enumerate(hlaFile):
            if n == 0:
                variables = line.strip().split(',')
                
                for i in range(1,int(((len(variables)-2)/3))+1):
                    FileName = variables[i*3]
                    Idx = FileName.find('.')
                    FileName = FileName[0:Idx] + '.csv'
                    AlleleFishersExactOddsRatio(CSVInPath, ControlTablePath, OutFolderPath, FileName, ((i*3)-2), ((i*3)-1))


parser = argparse.ArgumentParser(description='Counts and Calculates the number of Alleles in a file and its Frequency along with calculating Fishers Exact and Odds Ratio')
parser.add_argument('-CSVInPath','--CSVInPath', type = str, metavar='', help = 'The Path to your CSV File with Alleles', required=True)
parser.add_argument('-ControlTablePath','--ControlTablePath', type = str, metavar='', help = "The Path to your Allele Control Table", required=True)
parser.add_argument('-OutFolderPath','--OutFolderPath', type = str, metavar='', help = "The Path to where you want your folder to be created", required=True)

args = parser.parse_args()


FishersExactOddsRatio(args.CSVInPath, args.ControlTablePath, args.OutFolderPath)
