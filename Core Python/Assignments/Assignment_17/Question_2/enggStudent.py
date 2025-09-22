from student import Student

### 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
#     i. Branch
#     ii. InternalMarks
# b. Add the following methods
#     i. Parameterized constructor
#     ii. Display
#     iii. Accept
#     iv. override Method CalculateRank
#     v. Override __str__ Method


class EnggStudent(Student):

    def __init__(
        self,
        student_id="STD-000",
        name="Default",
        age=20,
        percentage=53,
        branch="Mechanical",
        internal_marks=20,
    ):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def display(self):
        super().display()
        print(
            f"""
Branch         : {self.branch}
Internal Marks : {self.internal_marks}
-----------------------------------------
Final Score    : {self.score:.2f}
-----------------------------------------
        """
        )

    def accept(self):
        super().accept()
        self.branch = input("Enter the Branch ::")
        self.internal_marks = int(input("Enter Internal Marks out-of 20 ::"))

    def calculateRank(self):
        self.score = (0.8 * self.percentage) + self.internal_marks
        if self.score >= 90.0:
            return "GRADE-A+"
        elif self.score >= 75.0:
            return "GRADE-A"
        elif self.score >= 60.0:
            return "GRADE-B"
        elif self.score >= 50.0:
            return "GRADE-C"
        else:
            return "GRADE-Fail"

    def __str__(self):
        return f"EnggStudent({self.student_id}, {self.name}, Age={self.age}, Percentage={self.percentage}%, Branch={self.branch}, InternalMarks={self.internal_marks})"


s1 = EnggStudent("E101", "Ansh", 17, 65, "Computer", 19)
s2 = EnggStudent("E102", "Hydra", 20, 92, "Mechanical", 18)
s3 = EnggStudent()

s1.display()
s2.display()
s3.display()

print(s1)
print(s2)
print(s3)