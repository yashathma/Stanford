
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

import os

#python3 /Users/yash/Desktop/StanfordCode/HLAStatistics/FEOR/FishersExactOddsRatio.py -CSVInPath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv -ControlTablePath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv -OutFolderPath /Users/yash/Desktop/StanfordCode/HLAStatistics/CSVInFishersOdds


def AlleleFishersExactOddsRatio(CSVInPath, ControlTablePath, OutFolderPath, FileName, A1, A2):
    CSVIn = CSVInPath
    DXTable = ControlTablePath
    
    Controls = []
    Cases = []

    NewControls = []
    NewCases = []

    with open(CSVIn) as csvIn:
        with open(DXTable) as dxTable:
            for n, line in enumerate(dxTable):
                if (n>0):
                    rowParse = line.strip().split(',')
                    if (rowParse[1] == '1'):
                        Controls.append(rowParse[0])
                    else:
                        Cases.append(rowParse[0])
                    
            for n, line in enumerate(csvIn):
                if (n>0):
                    rowParse = line.strip().split(',')

                    if(Controls.count(rowParse[0])>0):
                        NewControls.append(rowParse[A1])
                        NewControls.append(rowParse[A2])
                    else:
                        NewCases.append(rowParse[A1])
                        NewCases.append(rowParse[A2])


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
