import csv

with open('test.csv') as f:
    reader = csv.DictReader(f,delimiter=";")
    for row in reader:
        print(row)
        print(row['id'], row['tittle'])