a = input("enter a sentence")
print(a)
sentencesplit = a.split()
print(sentencesplit)
uniqueword = set(sentencesplit)
for i in uniqueword:
    print(f"{i} occurs {sentencesplit.count(i)}")
