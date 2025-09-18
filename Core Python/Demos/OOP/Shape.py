### shape inheritance

class Shape:

    def __init__(self, id, area):
        self.id=id
        self.area=area
        
    def display(self):
        print("ID ::" , self.id)
        print("AREA ::", self.area)

class Rectangle(Shape):

    def __init__(self, id, area,length,breadth):
        super().__init__(id, area)
        self.length=length
        self.breadth=breadth

    def display(self):
        super().display()
        print("Length ::", self.length)
        print("Breadth ::", self.breadth)

rect= Rectangle("101-Rect", 800,20,40)

rect.display()