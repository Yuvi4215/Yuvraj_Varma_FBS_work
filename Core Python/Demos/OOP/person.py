class Person:

    def setData(self, name, age ,add):
        self.name=name
        self.age=age
        self.add=add

    def displayData(self):
        print("Name ::" ,self.name)
        print("Age ::" ,self.age)
        print("Address ::" ,self.add)
        print("-----------------------------")

p1=Person()
p1.setData("Alpha", 99.22, "maths")
p1.displayData()

p2= Person()
p2.setData("Pi", 3.1415, "maths")
p2.displayData()