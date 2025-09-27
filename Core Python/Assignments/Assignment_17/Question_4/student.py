from college import College

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"Student:({self.student_id}, {self.name}, Age={self.age}, Percentage={self.percentage}%)"


s1 = Student("S101", "Thor Sharma", 20, 85)
s2 = Student("S102", "Hulk Sethi", 19, 78)
s3 = Student("S103", "Hydra Singh", 21, 90)
s4 = Student("S104", "Wonda Iyer", 18, 72)
s5 = Student("S105", "Spider Mehta", 22, 88)
s6 = Student("S106", "Blade Reddy", 20, 65)
s7 = Student("S107", "Yuvraj Varma", 19, 95)

college = College(9)

college.addStudent(s1)
college.addStudent(s2)
college.addStudent(s3)
college.addStudent(s4)
college.addStudent(s5)
college.addStudent(s6)
college.addStudent(s7)

print(
    f"""
--------------------------------------------------- 
All Students in College
---------------------------------------------------
{college}
"""
)


print(
    f"""
--------------------------------------------------- 
Get Student S103
--------------------------------------------------- 
{college.getStudent("S103")}   
"""
)

print("Remove Student S105")
college.removeStudent("S105")

print(
    f"""
--------------------------------------------------- 
After Removal
--------------------------------------------------- 
{college}
"""
)
