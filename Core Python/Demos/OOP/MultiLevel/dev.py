from emp import Emp

class SoftwareDev(Emp):
    def __init__(self, name, age, id, sal,proj,span):
        super().__init__(name, age, id, sal)
        self.proj=proj
        self.span=span
    
    def display(self):
        return super().display()+f"\nProject:: {self.proj}\nProject Span:: {self.span} Months"
    
s1=SoftwareDev("Yuvraj", 27, "101",69000, "Python", 6)
print(s1.display())