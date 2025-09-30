### Sub class/Derived class
from emp import Emp


class Dev(Emp):

    def __init__(self, id, name, basic_sal, bonus=2000, dept="S/W Developer", total_sal=0):
        super().__init__(id, name, basic_sal, dept)
        self.bonus=bonus
        self.total_sal = self.calculateSalary()

    def calculateSalary(self):
        da_amt = 0.1 * self.basic_sal
        hra_amt = 0.12 * self.basic_sal
        # print(f"DA: {da_amt}, HRA : {hra_amt}, Bonous : {self.bonus}")
        return da_amt + hra_amt + self.basic_sal + self.bonus

# d1=Dev("101","Yuvi",69000,2200)
# print(d1)