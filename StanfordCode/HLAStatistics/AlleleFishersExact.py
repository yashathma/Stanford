
from scipy.stats import fisher_exact

import numpy as np

from collections import Counter
import argparse

from collections import Counter
import argparse

#python3 /Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleFishersExact.py -CSVInPath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv -ControlTablePath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv -OutFilePath /Users/yash/Desktop/StanfordCode/HLAStatistics/Test.csv


def AlleleCountFrequencyFishersExact(CSVInPath, ControlTablePath, OutFilePath):
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
                        NewControls.append(rowParse[1])
                        NewControls.append(rowParse[2])
                    else:
                        NewCases.append(rowParse[1])
                        NewCases.append(rowParse[2])


    controlsCount = Counter(NewControls)

    notControlsCount = Counter(NewCases)

    keys = list(controlsCount.keys())


    outFile = open(OutFilePath, 'w')

    outFile.write(','.join(['Allele','Control', 'ControlFrequency', 'Case', 'CaseFrequency','Pvalue','OddsRatio']))
    outFile.write('\n')
    
    for n in range(0,len(keys)-1):
        oddsRatio, pValue = fisher_exact([[notControlsCount[keys[n]],1000-notControlsCount[keys[n]]],[controlsCount[keys[n]],3000-controlsCount[keys[n]]]])
        outFile.write(str(keys[n])+','+str(controlsCount[keys[n]])+','+ str((controlsCount[keys[n]])/(len(Controls+Cases)*2)) +','+str(notControlsCount[keys[n]])+','+ str((notControlsCount[keys[n]])/(len(Controls+Cases)*2))+','+str(pValue)+','+str(oddsRatio)+'\n')



parser = argparse.ArgumentParser(description='Counts and Calculates the number of Alleles in a file and its Frequency')
parser.add_argument('-CSVInPath','--CSVInPath', type = str, metavar='', help = 'The Path to your CSV File with Alleles', required=True)
parser.add_argument('-ControlTablePath','--ControlTablePath', type = str, metavar='', help = "The Path to your Allele Control Table", required=True)
parser.add_argument('-OutFilePath','--OutFilePath', type = str, metavar='', help = "The Path to where you want your file to be created", required=True)

args = parser.parse_args()




AlleleCountFrequencyFishersExact(args.CSVInPath, args.ControlTablePath, args.OutFilePath)







# #for Allele A11
# oddsRatio, pValue = fisher_exact([[215,1000-215],[82,3000-82]])


#AlleleCountFrequency(args.CSVInPath, args.ControlTablePath, args.OutFilePath)


# print(oddsRatio)
# print(pValue)