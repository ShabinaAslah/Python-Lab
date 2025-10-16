def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
num=int(input("enter a num:"))
if num<0:
    print("factorial is not defined for given -ve num")
elif num==0:
    print(f"{num}!=1")
else:
    fact=fac(num)
    print(f"{num}!={fact}")
