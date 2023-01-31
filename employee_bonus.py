import csv
infile = open('employeepay.csv', 'r')
reader = csv.reader(infile)


for row in reader:
    print('ID:',row[0])
    print('First name:',row[1])
    print('Last name:',row[2])
    print('Salary:',row[3])
    print('Bonus:',row[4])
    print()



