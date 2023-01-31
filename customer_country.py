import csv
infile = open('customer.csv','r')
outfile = open('customer_country.csv','w')
reader = csv.reader(infile)
writer = csv.writer(outfile)


for row in reader:
    print("ID",row[0])
    print("First Name",row[1])
    print("Last Name:",row[2])
    print("City",row[3])
    print("Country",row[4])
    print("Phone",row[5])


