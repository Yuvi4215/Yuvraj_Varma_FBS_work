### Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:

    def __init__(self, student_id="STD-000", name="Default", age=20, percentage=53):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def display(self):
        print(
            f"""
-----------------------------------------
Student ID   : {self.student_id}
Name         : {self.name}
Age          : {self.age}
Percentage   : {self.percentage}%
-----------------------------------------
Rank         : {self.calculateRank()}
-----------------------------------------"""
        )

    def accept(self):
        # print("Accept()")
        self.student_id=input("Enter Student ID :: ")
        self.name=input("Enter the Name :: ")
        self.age=int(input("Enter the Age :: "))
        self.percentage=float(input("Enter the Percentage :: "))

    def calculateRank(self):
        # print("calculateRank()")
        if self.percentage>=90.0:
            return "GRADE-A+"
        elif self.percentage >= 75.0:
            return "GRADE-A"
        elif self.percentage >= 60.0:
            return "GRADE-B"
        elif self.percentage >= 50.0:
            return "GRADE-C"
        else:
            return "GRADE-Fail"
    
    def __str__(self):
        # print("__str__()")
        return f"Student({self.student_id}, {self.name}, Age={self.age}, Percentage={self.percentage}%, Rank={self.calculateRank()})"

s1 = Student("STD-101", "Batman", 32, 89)
s2 = Student("STD-102", "Thor", 22, 63)
s3 = Student("STD-103", "Ironman", 12, 95)
s4 = Student("STD-104", "Vision", 35, 45)
s5=Student()

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)