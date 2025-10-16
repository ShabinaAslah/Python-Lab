def cc(ins):
    count={}
    for c in ins:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
    return count
s=input("enter a string:")
r=cc(s)
print(r)
