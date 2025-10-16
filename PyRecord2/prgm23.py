def ep(s,e):
    esq=[]
    for n in range(s,e+1):
        if all(int(d)%2==0
               for d in str(n)):
                    sq=int(n**0.5)
                    if sq*sq==n:
                        esq.append(n)
    return esq
s=1000
e=9999
r=ep(s,e)
print(r)
