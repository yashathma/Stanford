print("START")
import csv
import array


class HLA:

    def __init__(self, A1, A2, A_prob, B1, B2, B_prob, C1, C2, C_prob, DPB1_1, DPB1_2, DPB1_prob, DQA1_1, DQA1_2, DQA1_prob, DQB1_1, DQB1_2, DQB1_prob, DRB1_1, DRB1_2, DRB1_prob, DPA1_1, DPA1_2, DPA1_prob, DRB3_1, DRB3_2, DRB3_prob, DRB4_1, DRB4_2, DRB4_prob, DRB5_1, DRB5_2, DRB5_prob, ArrayID):
        self.A1 = A1
        self.A2 = A2
        self.A_prob = A_prob

        self.B1 = B1
        self.B2 = B2
        self.B_prob = B_prob

        self.C1 = C1
        self.C2 = C2
        self.C_prob = C_prob

        self.DPB1_1 = DPB1_1
        self.DPB1_2 = DPB1_2
        self.DPB1_prob = DPB1_prob

        self.DQA1_1 = DQA1_1
        self.DQA1_2 = DQA1_2
        self.DQA1_prob = DQA1_prob

        self.DQB1_1 = DQB1_1
        self.DQB1_2 = DQB1_2
        self.DQB1_prob = DQB1_prob

        self.DRB1_1 = DRB1_1
        self.DRB1_2 = DRB1_2
        self.DRB1_prob = DRB1_prob

        self.DPA1_1 = DPA1_1
        self.DPA1_2 = DPA1_2
        self.DPA1_prob = DPA1_prob

        self.DRB3_1 = DRB3_1
        self.DRB3_2 = DRB3_2
        self.DRB3_prob = DRB3_prob

        self.DRB4_1 = DRB4_1
        self.DRB4_2 = DRB4_2
        self.DRB4_prob = DRB4_prob

        self.DRB5_1 = DRB5_1
        self.DRB5_2 = DRB5_2
        self.DRB5_prob = DRB5_prob

        self.ArrayID = ArrayID

    def getA1(self):
        return self.A1

    def getA2(self):
        return self.A2

    def getA_prob(self):
        return self.A_prob

    def getB1(self):
        return self.B1

    def getB2(self):
        return self.B2

    def getB_prob(self):
        return self.B_prob

    def getC1(self):
        return self.C1

    def getC2(self):
        return self.C2

    def getC_prob(self):
        return self.C_prob

    def getDPB1_1(self):
        return self.DPB1_1

    def getDPB1_2(self):
        return self.DPB1_2

    def getDPB1_prob(self):
        return self.DPB1_prob

    def getDQA1_1(self):
        return self.DQA1_1

    def getDQA1_2(self):
        return self.DQA1_2

    def getDQA1_prob(self):
        return self.DQA1_prob

    def getDQB1_1(self):
        return self.DQB1_1

    def getDQB1_2(self):
        return self.DQB1_2

    def getDQB1_prob(self):
        return self.DQB1_prob

    def getDRB1_1(self):
        return self.DRB1_1

    def getDRB1_2(self):
        return self.DRB1_2

    def getDRB1_prob(self):
        return self.DRB1_prob

    def getDPA1_1(self):
        return self.DPA1_1

    def getDPA1_2(self):
        return self.DPA1_2

    def getDPA1_prob(self):
        return self.DPA1_prob

    def getDRB3_1(self):
        return self.DRB3_1

    def getDRB3_2(self):
        return self.DRB3_2

    def getDRB3_prob(self):
        return self.DRB3_prob

    def getDRB4_1(self):
        return self.DRB4_1

    def getDRB4_2(self):
        return self.DRB4_2

    def getDRB4_prob(self):
        return self.DRB4_prob

    def getDRB5_1(self):
        return self.DRB5_1

    def getDRB5_2(self):
        return self.DRB5_2

    def getDRB5_prob(self):
        return self.DRB5_prob

    def getArrayID(self):
        return self.ArrayID














print("Copying...")

hla = []

with open('HLAIn.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        hla.append(HLA(
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
            line[7],
            line[8],
            line[9],
            line[10],
            line[11],
            line[12],
            line[13],
            line[14],
            line[15],
            line[16],
            line[17],
            line[18],
            line[19],
            line[20],
            line[21],
            line[22],
            line[23],
            line[24],
            line[25],
            line[26],
            line[27],
            line[28],
            line[29],
            line[30],
            line[31],
            line[32],
            line[33],
            line[34]))


            #put the write in here


            

print("Copied")





















print("WRITING...")

with open('HLAOut.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    

    for i in range(1, len(hla)):
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'A.1', str(hla[i].getA1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'A.2', str(hla[i].getA2())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'A.prob', str(hla[i].getA_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'B.1', str(hla[i].getB1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'B.2', str(hla[i].getB2())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'B.prob', str(hla[i].getB_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'C.1', str(hla[i].getC1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'C.2', str(hla[i].getC2())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'C.prob', str(hla[i].getC_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DPB1.1', str(hla[i].getDPB1_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DPB1.2', str(hla[i].getDPB1_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DPB1.prob', str(hla[i].getDPB1_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DQA1.1', str(hla[i].getDQA1_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DQA1.2', str(hla[i].getDQA1_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DQA1.prob', str(hla[i].getDQA1_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DQB1.1', str(hla[i].getDQB1_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DQB1.2', str(hla[i].getDQB1_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DQB1.prob', str(hla[i].getDQB1_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB1.1', str(hla[i].getDRB1_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB1.2', str(hla[i].getDRB1_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DRB1.prob', str(hla[i].getDRB1_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DPA1.1', str(hla[i].getDPA1_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DPA1.2', str(hla[i].getDPA1_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DPA1.prob', str(hla[i].getDPA1_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB3.1', str(hla[i].getDRB3_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB3.2', str(hla[i].getDRB3_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DRB3.prob', str(hla[i].getDRB3_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB4.1', str(hla[i].getDRB4_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB4.2', str(hla[i].getDRB4_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DRB4.prob', str(hla[i].getDRB4_prob())])

        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB5.1', str(hla[i].getDRB5_1())])
        thewriter.writerow(
            ['HLA_'+str(i), hla[i].getArrayID(), 'DRB5.2', str(hla[i].getDRB5_2())])
        thewriter.writerow(['HLA_'+str(i), hla[i].getArrayID(),
                            'DRB5.prob', str(hla[i].getDRB5_prob())])

print("DONE")





