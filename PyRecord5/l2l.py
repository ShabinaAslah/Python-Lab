l1=[]
with open('test.txt','r') as f1:
    for ln1 in f1:
        l1.append(ln1.split())
print(l1)
