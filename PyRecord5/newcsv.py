import csv
csv_col=['ID','NAME','COUNTRY']
dict_data=[{'ID':1,'NAME':'IRFANA','COUNTRY':'INDIA'},
         {'ID':2,'NAME':'MARIYA','COUNTRY':'INDIA'},
         {'ID':3,'NAME':'SHABINA','COUNTRY':'INDIA'}]
csv_file="Name.csv"
try:
    with open(csv_file,'w')as f1:
        writer=csv.DictWriter(f1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")

data1=csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
