def ff(num):
    f=[]
    for i in range(1,num+1):
        if num%i==0:
            f.append(i)
    return f
n=int(input("enter the number of row:"))
r=ff(n)
print(f"the factor of {n} are:{r}")
