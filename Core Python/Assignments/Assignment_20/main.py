from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks


class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def total_computer_marks(self):
        return (
            self.sy_marks.computer_total
            + self.ty_marks.theory
            + self.ty_marks.practical
        )

    def percentage(self):
        return (self.total_computer_marks() / 300) * 100

    def grade(self):
        p = self.percentage()
        if p >= 70:
            return "A"
        if p >= 60:
            return "B"
        if p >= 50:
            return "C"
        if p >= 40:
            return "Pass Class"
        return "Fail"

    def display(self):
        print(f"""
------------------- Student Result -------------------
Roll No        : {self.roll_no}
Name           : {self.name}
------------------------ SY --------------------------
Computer       : {self.sy_marks.computer_total}
Maths          : {self.sy_marks.maths_total}
Electronics    : {self.sy_marks.electronics_total}
------------------------ TY  -------------------------
Theory         : {self.ty_marks.theory} 
Practical      : {self.ty_marks.practical}
Computer Total : {self.total_computer_marks()}
Percentage     : {self.percentage():.2f} %
----------------------- GRADE ------------------------
Grade          : {self.grade()}
------------------------------------------------------""")


if __name__ == "__main__":
    sy = SYMARKS(89, 85, 92)
    ty = TYMarks(70, 65)
    s = Student(101, "spider Mehta", sy, ty)
    s.display()
