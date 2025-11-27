import csv
with open('student.csv',newline="")as csvf1:
    data=csv.DictReader(csvf1)
    print("NAME")
    print("_____")
    for i in data:
        print(i['NAME'])
