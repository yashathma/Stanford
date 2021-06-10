from collections import Counter

CSVIn = '/Users/yash/Desktop/StanfordCode/HLAStatistics/CSVIn.csv'
DXTable = '/Users/yash/Desktop/StanfordCode/HLAStatistics/DXTable.csv'



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
                rowParse = line.strip().split(',')
                A.append(rowParse[1])
                A.append(rowParse[2])

Aindex = 0
for n in range(0,len(controls)):
    if int(controls[n]) == 1:
        AControl.append(A[Aindex])
        AControl.append(A[Aindex+1])
    else:
        AnotControl.append(A[Aindex])
        AnotControl.append(A[Aindex+1])

    Aindex+=2

controlsCount = Counter(AControl)

notControlsCount = Counter(AnotControl)

keys = list(controlsCount.keys())


outFile = open('/Users/yash/Desktop/StanfordCode/HLAStatistics/ControlDox.csv', 'w')

outFile.write(','.join(['Allele','Control', 'Not Control']))
outFile.write('\n')



for n in range(0,len(keys)-1):
    outFile.write(str(keys[n])+','+str(controlsCount[keys[n]])+','+str(notControlsCount[keys[n]])+'\n')


 



              
                        
     