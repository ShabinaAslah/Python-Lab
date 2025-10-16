def lw(w):
    max=len(w[0])
    for i in w:
        l=len(i)
        if l>max:
            max=l
    return max
w=input("enter a list of words separated by space:")
w=w.split()
r=lw(w)
print(f"the length of the longest word is:{r}")
    
