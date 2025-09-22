from student import Student

### 3. Create a class MedicalStudent inherited from Student with following:
# Data members :
#   i.Specialization
#   ii. MarksOfInternship
# b. Add the following methods :
#   i. Parameterized constructor
#   ii. Display
#   iii. Accept
#   iv. override Method CalculateRank
#   v. Override __str__ Method


class MedicalStudent(Student):
    def __init__(
        self,
        student_id="STD-101",
        name="Default",
        age=20,
        percentage=83,
        specialization="Heart",
        marks_of_internship=35,
    ):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    def display(self):
        super().display()
        print(
            f"""
Specialization  : {self.specialization}
Internship Marks: {self.marks_of_internship}
-----------------------------------------
Final Rank(T+P) : {self.calculateRank()}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
"""
        )

    def accept(self):
        super().accept()
        self.specialization = input("Enter the Specialization :")
        self.marks_of_internship = int(input("Enter Marks of Internship out of 40 :"))

    def calculateRank(self):
        final_score = (self.percentage * 0.6) + (self.marks_of_internship * 0.4)
        # print(final_score)
        if final_score >= 90.0:
            return "GRADE-A+"
        elif final_score >= 75.0:
            return "GRADE-A"
        elif final_score >= 60.0:
            return "GRADE-B"
        elif final_score >= 50.0:
            return "GRADE-C"
        else:
            return "GRADE-Fail"

    def __str__(self):
        return f"MedicalStudent(Student ID:{self.student_id}, Name:{self.name}, Age:{self.age}, Percentage:{self.percentage}, Specialization:{self.specialization}, Internship Marks:{self.marks_of_internship})"


# Creating individual medical students
m1 = MedicalStudent("M101", "Ansh", 17, 91, "Gastroenterology", 89)
m2 = MedicalStudent("M102", "Hydra", 19, 85, "Cardiology", 97)
m3 = MedicalStudent("M103", "Rohan", 20, 72, "Neurology", 78)
m4 = MedicalStudent("M104", "Meera", 18, 69, "Pediatrics", 64)
m5 = MedicalStudent("M105", "Arjun", 21, 69, "Orthopedics", 70)
m6 = MedicalStudent("M106", "Kavya", 19, 56, "Dermatology", 57)
m7 = MedicalStudent("M107", "Ishaan", 22, 35, "Oncology", 22)

# Displaying details
m1.display()
m2.display()
m3.display()
m4.display()
m5.display()
m6.display()
m7.display()


print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
print(m7)
