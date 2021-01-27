import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py data.csv sequence.txt")

data = []
# names of people
names = []
# dna strands names
strand = []
# str count, num of repeats for each strands
STRcount = []
person = {}
nestedList = []
with open(sys.argv[1], 'r') as datafile:
    datareader = csv.DictReader(datafile)
    for row in datareader:
        data.append(row)
        
        # list for names
        names.append(row["name"])
    for key in row.keys():
        strand.append(key)
    # remove name so all left with strands
    strand.remove('name')

    ######nested dict######
    for row in data:
        del row['name']
        nestedList.append(row)
    person = {names[i]: nestedList[i] for i in range(len(nestedList))}
###############PROCESS SEQUENCE#################################
# DNA SEQUENCE
sequence = []
# dict with scanned val from sequence
myDict = {} 

count = 0
with open(sys.argv[2], 'r') as sequencefile:
    sequencereader = csv.reader(sequencefile)
    for row in sequencereader:
        sequence = row
        # print(len(row[0]))
        sequencestring = ''.join(str(i)for i in sequence)
        # print(sequencestring)

        for j in strand:
            i = 0
            maxcount = 0
            while i < len(sequencestring):
                window = sequencestring[i:i+len(j)]

                if window == j:
                    count += 1
                    
                    # check max value
                    if count > maxcount:
                        maxcount = count
                    i += len(j)
                else:
                    count = 0
                    i += 1
                    
            # turn num to string to compare later on
            myDict[j] = str(maxcount)

############COMPARE PROCESSED SEQUENCE DATA TO DATABASE##################
        # print(f"myDict:{myDict}")
        finalDict = {}
        switch = 0
        # put into a nested dictionary to compare with OG data
        finalDict['name'] = myDict

        for check in person:
            for final in finalDict:
                if(person[check] == finalDict[final]):
                    print(f"{check}\n")
                    exit(0)
        print("no match")