### Sub class/Derived class
from emp import Emp

class Admin(Emp):

    def __init__(self, id, name, basic_sal,allownce=2600, dept="Admin", total_sal=0):
        super().__init__(id, name, basic_sal, dept)
        self.allownce=allownce
        self.total_sal=self.calculateSalary()

    def calculateSalary(self):
        da_amt=0.10* self.basic_sal
        hra_amt=0.13* self.basic_sal
        # print(f"DA: {da_amt}, HRA : {hra_amt}, Allownce : {self.allownce}")
        return (da_amt+hra_amt+self.basic_sal+ self.allownce)
    
# a1=Admin("101","Yuvi",69000,2200)
# print(a1)

