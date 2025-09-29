### 
from emp import Emp

class HR(Emp):

    def __init__(self, id, name, basic_sal,comm=3850, dept="HR", total_sal=0):
        super().__init__(id, name, basic_sal, dept)
        self.comm=comm
        self.total_sal=self.calculateSalary()
    
    def calculateSalary(self):
        da_amt=0.11*self.basic_sal
        hra_amt=0.13*self.basic_sal
        # print(f"DA: {da_amt}, HRA : {hra_amt}, Commision : {self.comm}")
        return (da_amt + hra_amt+self.basic_sal+ self.comm)
    
# h1=HR("101","Yuvi",69000,2200)
# print(h1)