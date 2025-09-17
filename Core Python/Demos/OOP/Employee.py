### Employee

class Employee:

    def __init__(self,id, name, sal, deprt ):
        print("Constructor is called ::")
        self.eid=id
        self.ename=name
        self.salary=sal
        self.dept=deprt

    def getData(self):
        return f"Epmloyee\n EID::{self.eid}\n NAME::{self.ename}\nSALARY::{self.salary}\nDEPT::{self.dept}"

    def __del__(self):
        print(f"Destroy function is called ::{self}")


e1= Employee(101, "Spider-man", 11.50, "marvel")
print(e1.getData())
del e1
print("####################################")
print("\n\n")
e2= Employee(111, "Thor", 9.50, "Asguard")
print(e2.getData())
print("####################################")