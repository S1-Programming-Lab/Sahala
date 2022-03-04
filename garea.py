from Graphics.Rectfunctions import*
from Graphics.cirfunctions import*
from Graphics.DGraphics.spherefunctions import*
1=int(input("enter 1"))
b=int(input("enter b"))
print("area=",RectArea(1,b))
print("perimeter=",Rectperimeter(1,b))
r=int(input("enetr the radius of a circle"))
print("circle area =",cirArea(r))
print("circle perimeter=",cirperimeter(r))
r=int(input("enter radius of sphere"))
print("circle area=",SpArea(r))
print("circle perimeter=",SpPerimeter(r))
