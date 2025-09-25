### __str__() override

class EMP:
    def __init__(self,id,name,sal,dept):
        self.id=id
        self.name=name
        self.sal=sal
        self.dept=dept

    def __str__(self):
        return f"""
ID         :: {self.id}
Name       :: {self.name}
Salary     :: {self.sal}
Department :: {self.dept}
"""
    

e1=EMP("101", "Employee-default", 690000, "Data-Ai")
print(e1)