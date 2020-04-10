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

# Fills in DNA_dict
with open(argv[2], 'r') as DNA:
    for line in DNA:
        for s in range(len(list)):
            for i in range(len(line)):
                y = 0
                k = i
                while True:
                    if line[k: k + len(list[s])] == list[s]:
                        k += len(list[s])
                        y += 1
                    else:
                        break
                    if y > DNA_dict[list[s]]:
                        DNA_dict[list[s]] = y

# Compares DNA_dict with all the rows of data.csv except the first row
with open(argv[1], 'r') as data:
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        y = 0
        for s in range(len(list)):
            if int(row[s + 1]) != int(DNA_dict[f'{list[s]}']):
                y += 1
                #print(row[s + 1], end="")
                #print (DNA_dict[f'{list[s]}'])
        if y == 0:
            print(row[0])
            exit()
    print("No match")
