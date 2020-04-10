from sys import argv, exit
import csv
import copy

# Rejects if not exactly 2 command-line arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Creates keys of DNA_dict (the dict which stores DNA STR profile of DNA we are sequencing)        
list = []
with open(argv[1], 'r') as data:
    reader = csv.DictReader(data)
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

# Compares DNA_dict with all the rows of data.csv except the first row, outputting the name field of the row in which there is an exact match
with open(argv[1], 'r') as data:
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        y = 0
        for s in range(len(list)):
            if int(row[s + 1]) != int(DNA_dict[f'{list[s]}']):
                y += 1
        if y == 0:
            print(row[0])
            exit()
    print("No match")
