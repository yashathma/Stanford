from collections import Counter

# PERSONAL NOTES

# Input CSV Path
# /Users/yash/Desktop/StanfordCode/HLAStatistics/CSVIn.csv

# Input Control Table Path
# /Users/yash/Desktop/StanfordCode/HLAStatistics/DXTable.csv

# Where I want my file Created
# /Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleCount&Freq.csv

# Terminal Command
# python /Users/yash/Desktop/StanfordCode/HLAStatistics/AlleleFrequency.py -CSVInPath /Users/yash/Desktop/StanfordCode/HLAStatistics/CSVIn.csv -ControlTablePath /Users/yash/Desktop/StanfordCode/HLAStatistics/DXTable.csv -OutFilePath /Users/yash/Desktop/StanfordCode/HLAStatistics/Test.csv

# Function Input Example
# AlleleCountFrequency('/Users/yash/Desktop/StanfordCode/HLAStatistics/CSVIn.csv','/Users/yash/Desktop/StanfordCode/HLAStatistics/DXTable.csv','/Users/yash/Desktop/StanfordCode/HLAStatistics/Test.csv')


def AlleleCountFrequency(CSVInPath, ControlTablePath, OutFilePath):
    CSVIn = CSVInPath
    DXTable = ControlTablePath


    controls = []
    A = []

    AControl = []
    AnotControl = []

        
    with open(CSVIn) as csvIn:
        with open(DXTable) as dxTable:
            for n, line in enumerate(dxTable):
                if n == 0:
                    variables = line.strip().split(',')
                
                else:
                    rowParse = line.strip().split(',')
                    controls.append(rowParse[1])
                    


            for n, line in enumerate(csvIn):
                if n == 0:
                    variables = line.strip().split(',')
                
                else:
                    if(controls[n-1] == str(1)):
                        rowParse = line.strip().split(',')
                        AControl.append(rowParse[1])
                        AControl.append(rowParse[2])

                    else:
                        rowParse = line.strip().split(',')
                        AnotControl.append(rowParse[1])
                        AnotControl.append(rowParse[2])


    controlsCount = Counter(AControl)

    notControlsCount = Counter(AnotControl)

    keys = list(controlsCount.keys())


    outFile = open(OutFilePath, 'w')

    outFile.write(','.join(['Allele','Control', 'ControlFrequency', 'Case', 'CaseFrequency']))
    outFile.write('\n')



    for n in range(0,len(keys)-1):
        outFile.write(str(keys[n])+','+str(controlsCount[keys[n]])+','+ str((controlsCount[keys[n]])/(len(controls)*2)) +','+str(notControlsCount[keys[n]])+','+ str((notControlsCount[keys[n]])/(len(controls)*2))+'\n')




import argparse

parser = argparse.ArgumentParser(description='Counts and Calculates the number of Alleles in a file and its Frequency')
parser.add_argument('-CSVInPath','--CSVInPath', type = str, metavar='', help = 'The Path to your CSV File with Alleles', required=True)
parser.add_argument('-ControlTablePath','--ControlTablePath', type = str, metavar='', help = "The Path to your Allele Control Table", required=True)
parser.add_argument('-OutFilePath','--OutFilePath', type = str, metavar='', help = "The Path to where you want your file to be created", required=True)

args = parser.parse_args()

AlleleCountFrequency(args.CSVInPath, args.ControlTablePath, args.OutFilePath)