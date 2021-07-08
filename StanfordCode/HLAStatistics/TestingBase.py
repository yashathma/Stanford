import pandas as pd

A1 = 1
A2 = 2

dx = pd.read_csv('/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/DXTable.csv')

CSVIN = pd.read_csv('/Users/yash/Desktop/StanfordCode/HLAStatistics/BaseFiles/CSVIn.csv')

NewCases = []
NewControls = []

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
