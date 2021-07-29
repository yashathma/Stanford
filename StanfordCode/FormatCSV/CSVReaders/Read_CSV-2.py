
from collections import defaultdict

def OrganizeCSV(InFileName, OutFileName):
    FILE = InFileName
    outFile = open(OutFileName, 'w')
    
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

                        

       #HLA_1,1,A.1,NA                 
              
                        
     
        outFile.close()

        

OrganizeCSV('CSVFiles/CSV_1.csv', 'YashIsGreat.csv')

print('end') 

    






# edge cases




#Use Bash to read files


#make sure the number work
# argparse
# for the input of the file names
# errors

