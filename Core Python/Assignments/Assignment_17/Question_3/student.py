class Student:
    def __init__(self,student_id="STD-101", name="Default", age=20, percentage=83):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.percentage=percentage
    
    def display(self):
        print(f"""
-----------------------------------------
Student ID   : {self.student_id}
Student Name : {self.name}
Student Age  : {self.age}
Percentage   : {self.percentage:.2f}%
-----------------------------------------
Rank         : {self.calculateRank()}
-----------------------------------------""")
    
    def accept(self):
        self.student_id=input("Enter Student ID : ")
        self.name=input("Enter Student Name :")
        self.age=int(input("Enter Student Age :"))
        self.percentage=float(input("Enter Percentage :"))

    def calculateRank(self):
        if self.percentage>=90.0:
            return "Grade-A+"
        elif self.percentage>=75.0:
            return "Grade-A"
        elif self.percentage>=60.0:
            return "Grade-B"
        elif self.percentage>=50.0:
            return "Grade-C"
        else:
            return "Grade-Fail"
    
    def __str__(self):
        # print("__str__()")
        return f"Student({self.student_id}, {self.name}, Age={self.age}, Percentage={self.percentage}%, Rank={self.calculateRank()})"


# s1 = Student("STD-101", "Batman", 32, 89)
# s2 = Student("STD-102", "Thor", 22, 63)
# s3 = Student("STD-103", "Ironman", 12, 95)
# s4 = Student("STD-104", "Vision", 35, 45)
# s5 = Student()

# s1=Student()
# s2=Student()
# s3=Student()
# s4=Student()
# s5=Student()

# s1.accept()
# s2.accept()
# s3.accept()
# s4.accept()
# s5.accept()



# s1.display()
# s2.display()
# s3.display()
# s4.display()
# s5.display()

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)