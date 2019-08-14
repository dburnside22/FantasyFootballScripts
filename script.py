import csv

qb = open('./qb.csv')
csv_qb = csv.reader(qb)

for row in csv_qb:
    print(row)
