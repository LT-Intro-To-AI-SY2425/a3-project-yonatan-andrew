import csv
with open('gen1.csv', 'r') as csvfile:
    pokereader = csv.DictReader(csvfile, delimiter=' ')
    for row in pokereader:
        print(row)
    