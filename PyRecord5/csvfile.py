import csv
with open('student.csv','r')as f1:
    reader=csv.reader(f1)
    for row in reader:
        print(row)
