from sys import argv, exit
import csv
import copy

# Rejects if not exactly 2 command-line arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Creates keys of DNA_dict (the dict which stores DNA STR profile of DNA we are sequencing)
# Copies database data into a nested dictionary megadict
list = []
megadict = {}
tempdict = {}
dictcount = 0
namedict = {}
with open(argv[1], 'r') as data:
    reader = csv.DictReader(data)
    for row in reader:
        tempdict = row
        tempname = tempdict['name']
        tempdict.pop('name')
        megadict[tempname] = tempdict
        namedict[dictcount] = tempname
        dictcount += 1
    list = reader.fieldnames
    list.pop(0)
        
DNA_dict = dict.fromkeys(list, 0)

# Checks how many times STR list[s] repeats starting from line[k]
def check(s, k, y):
    if line[k: k + len(list[s])] != list[s]:
        return y
    else:
        y +=1
        return check(s, k + len(list[s]), y)

# Fills in DNA_dict
with open(argv[2], 'r') as DNA:
    for line in DNA:
        for s in range(len(list)):
            for i in range(len(line)):
                y = 0
                k = i
                y = check(s, k, y)
                if y > DNA_dict[list[s]]:
                    DNA_dict[list[s]] = y

# Compares DNA_dict with all the dictionaries nested inside megadict
for x in range(dictcount):
    tmpdict = megadict[namedict[x]]
    dict = {}
    for s in range(len(list)):
        dict[list[s]] = int(tmpdict[f'{list[s]}'])
    if DNA_dict == dict:
        print(namedict[x])
        exit()
print("No match")
