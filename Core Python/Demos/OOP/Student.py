###Student 

class Student:
    count=0
    school_name="BBVS"
    address="Solapur"
    def __init__(self, name, cls, div):
        Student.count+=1
        self.std_name=name
        self.std_class=cls
        self.std_div=div

    def display(self):
        print(Student.school_name)
        print(Student.address)
        print(self.std_name)
        print(self.std_div)
        print(self.std_class)

    def getCount():
        print(f"Total count :: {Student.count}")
