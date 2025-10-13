y1=int(input("enter satarting year:"))
y2=int(input("enter the end year:"))
if y1>y2:
    print("end year must be grater than or equal to start year")
else:
    print(f"leap year from(y1)to{y2}")
    for y in range(y1,y2+1):
        if(y%4==0 and y%100!=0) or (y%400==0):
            print(y)
