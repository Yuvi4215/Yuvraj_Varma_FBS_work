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

