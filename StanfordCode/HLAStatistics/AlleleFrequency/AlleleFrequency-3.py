from collections import Counter

# PERSONAL NOTES

# Input CSV Path
# /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv

# Input Control Table Path
# /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv

# Where I want my file Created
# /Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleCount&Freq.csv

# Terminal Command
#python /Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleFrequency/AlleleFrequency-3.py -CSVInPath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv -ControlTablePath /Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv -OutFilePath /Users/yash/Desktop/StanfordCode/HLAStatistics/Test.csv

# Function Input Example
# AlleleCountFrequency('/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv','/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv','/Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleCount&Freq.csv')


def AlleleCountFrequency(CSVInPath, ControlTablePath, OutFilePath):
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

    outFile.write(','.join(['Allele','Control', 'ControlFrequency', 'Case', 'CaseFrequency']))
    outFile.write('\n')


    # controlcounting = 0
    # casecounting = 0
    
    for n in range(0,len(keys)-1):
        outFile.write(str(keys[n])+','+str(controlsCount[keys[n]])+','+ str((controlsCount[keys[n]])/(len(Controls+Cases)*2)) +','+str(notControlsCount[keys[n]])+','+ str((notControlsCount[keys[n]])/(len(Controls+Cases)*2))+'\n')
        # controlcounting += (controlsCount[keys[n]])/(len(Controls+Cases)*2)
        # casecounting += (notControlsCount[keys[n]])/(len(Controls+Cases)*2)


    # print(controlcounting)
    # print(casecounting)
    # print(casecounting+controlcounting)



import argparse

parser = argparse.ArgumentParser(description='Counts and Calculates the number of Alleles in a file and its Frequency')
parser.add_argument('-CSVInPath','--CSVInPath', type = str, metavar='', help = 'The Path to your CSV File with Alleles', required=True)
parser.add_argument('-ControlTablePath','--ControlTablePath', type = str, metavar='', help = "The Path to your Allele Control Table", required=True)
parser.add_argument('-OutFilePath','--OutFilePath', type = str, metavar='', help = "The Path to where you want your file to be created", required=True)

args = parser.parse_args()

AlleleCountFrequency(args.CSVInPath, args.ControlTablePath, args.OutFilePath)