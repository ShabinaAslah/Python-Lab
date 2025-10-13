import datetime
cy=datetime.date.today().year
fy=int(input("enter the final year:"))
if fy<cy:
    print("final year must be grater than or equal to current year")
else:
    print(f"leap year form {cy} to {fy}")
    for y in range(cy,fy+1):
        if(y%4==0 and y%100!=0) or (y%400==0):
            print(y)
