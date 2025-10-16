def ms(s):
    if s.endswith("ing"):
        return s+"ly"
    else:
        return s+"ing"
s=input("enter a string:")
r=ms(s)
print(r)
