sqa=lambda a:a**2
ra=lambda l,b:l*b
ta=lambda ba,h:0.5*ba*h

a=int(input("enter the length:"))
print("area of the sq:",sqa(a))

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("area of the triangle:",ra(l,b))

ba=int(input("enter the base:"))
h=int(input("enter the height:"))
print("area of rectangle:",ta(ba,h))
