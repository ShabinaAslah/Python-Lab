from Graphics.RectFun import *
from Graphics.CircleFun import *
from Graphics.Dgraphics.SpFun import *
from Graphics.Dgraphics.CubFun import *

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Rectangle Area:",RectArea(l,b))
print("Rectangle Perimeter:",RectPmeter(l,b))

r=int(input("Enter radius of circle:"))
print("Circle Area:",CirArea(r))
print("Circle Perimeter:",CirPmeter(r))

r=int(input("Enter radius of sphere:"))
print("Sphere Area:",SpArea(r))
print("Sphere Perimeter:",SpPmeter(r))

l=int(input("Enter cuboid length:"))
b=int(input("Enter cuboid breadth:"))
h=int(input("Enter cuboid height:"))
print("Cuboid Area:",CubArea(l,b,h))
print("Cuboid Perimeter:",CubPmeter(l,b,h))
