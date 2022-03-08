class Shape():
    def __init__(self,name,edgesno):
        self.name=name
        self.edgesno=edgesno
    def display(self):
        #print("nmae=",self.name)
        print("--Display EdgesNo.--")
        print("The no. of Edges Entered: ",self.edgesno)
class Rectangle(Shape):
    def __init__(self,name,edgesno,b,l):
        self.name=name
        self.edgesno=edgesno
        self.b=b
        self.l=l
    def area(self):
        area=self.b * self.l
        print("--Area Of Rectangle.--")
        print("Area of Rectangle is: ",area)
na=input("Enter Name\n")
ed=int(input("Enter no.of edges\n"))        
l1=int(input("Enter length of Rectangle\n"))
b1=int(input("Enter breadth of rectangle\n"))
obj=Rectangle(na,ed,b1,l1)
obj.display()
obj.area()

        
    
