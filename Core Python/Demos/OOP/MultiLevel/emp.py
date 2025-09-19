###
from person import Person

class Emp(Person):
    def __init__(self,name,age, id , sal):
        super().__init__(name,age)
        self.id=id
        self.sal=sal

    def display(self):
        return super().display()+f"\nID:: {self.id}\nSAL:: {self.sal}"

# e1=Emp("Yuvraj", 27, "101-Person", 50000)
# print(e1.display())