
from collections import defaultdict
import os

def OrganizeCSV(InFileName, OutFileName, OutFolderName):
    FILE = InFileName
    outFile = open('/Users/yash/Desktop/StanfordCode/FormatCSV'+'/'+OutFolderName+"/"+OutFileName, 'w')
    
    with open(FILE) as hlaFile:
        for n, line in enumerate(hlaFile):
            if n == 0:
                variables = line.strip().split(',')
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
    #Where to put your files
    path = "/Users/yash/Desktop/StanfordCode/FormatCSV"
    os.chdir(path)

    os.makedirs(OutFolderName)
    
    
    for files in os.walk(FolderDirectory):
        for f in files:
            for w in f:
                if len(w) > 1:
                    OutFile = "New"+ w
                    InFile = FolderDirectory+"/"+w
                    OrganizeCSV(InFile, OutFile, OutFolderName)

import argparse

parser = argparse.ArgumentParser(description='Retrieve Values for CSV Methods')
parser.add_argument('-FolderName','--folderName', type = str, metavar='', help = 'Name of Folder User wants to Reformat', required=True)
parser.add_argument('-NewFolderName','--newFolderName', type = str, metavar='', help = "The Name of the New Created Folder", required=True)

args = parser.parse_args()

OrganizeCSVFolder(args.folderName, args.newFolderName)

