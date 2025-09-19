### person 
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        return f"NAME:: {self.name}\nAGE:: {self.age}"
    
# p1=Person("Yuvraj", 27)
# print(p1.display())