from collections import defaultdict
import os

def OrganizeCSV(InFileName, OutFileName, OutFolderName):
    FILE = InFileName
    outFile = open(OutFolderName+"/"+OutFileName, 'w')
    
    with open(FILE) as hlaFile:
        for n, line in enumerate(hlaFile):
            if n == 0:
                variables = line.strip().split(',')
                print(variables)
                outFile.write(','.join(['IID','COH', 'Variable', 'Value']))
                outFile.write('\n')
            
            else:
                rowParse = line.strip().split(',')
                id = rowParse[0]
                COH = rowParse[-1]
                size = len(rowParse)

                for ind in range(1, size-1):
                    item = rowParse[ind]
                    var = variables[ind]
                    
                     


                    # checking variables
                    if ':' not in var or '0' not in var:

                        #checking prob
                        if 'prob' in var and '0.' in item:
                            outStr = '{},{},{},{}\n'.format(id, COH, var, item)
                            outFile.write(outStr)

                        #checking allele
                        elif 'prob' not in var and ':' in item:
                            outStr = '{},{},{},{}\n'.format(id, COH, var, item)
                            outFile.write(outStr)           
              
                        
     
        outFile.close()



def OrganizeCSVFolder(FolderDirectory, OutFolderName):
    path = "/Users/yash/VsCodeHelloWorld"
    os.chdir(path)

    os.makedirs(OutFolderName)
    
    
    for files in os.walk(FolderDirectory):
        for f in files:
            
            for w in f:
                if len(w) > 1:
                    OutFile = "New"+ w
                    InFile = FolderDirectory+"/"+w
                    OrganizeCSV(InFile, OutFile, OutFolderName)




OrganizeCSVFolder(input("What is the folder name?"), input("What would you like the new folder to be called?"))
