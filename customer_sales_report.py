import csv
infile = open('sales.csv', 'r')
outfile = open('salesreport.csv', 'w')

reader = csv.reader(infile, delimiter=",")
next(reader)

outfile.write('Customer ID'+','+'Calculated Total'+'\n')
outfile.write("_________________________________"+"\n")

cust_total = 0
cust_id = ""
for x in reader:
    if x[0] != cust_id:
        if cust_id:
            outfile.write(cust_id + "," +format(cust_total, ".2f") +"\n")
        cust_total = 0
        cust_id = x[0]
    subtotal = float(x[3])
    taxamount = float(x[4])
    freight = float(x[5])
    total = subtotal + taxamount + freight
    cust_total += total
outfile.write(cust_id + "," + str(format(cust_total, ".2f"))+ "\n")







