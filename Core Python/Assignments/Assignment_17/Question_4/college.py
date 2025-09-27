class College:
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []

    
    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student: {student.name} added successfully.")
        else:
            print(f"Cannot add student: {student.name} as College capacity reached.")

    
    def getStudent(self, student_id):
        for stnd in self.students:
            if stnd.student_id == student_id:
                return stnd
        print(f"Student with ID: {student_id} Not Found!")
        return None

    
    def removeStudent(self, student_id):
        for stnd in self.students:
            if stnd.student_id == student_id:
                self.students.remove(stnd)
                print(f"Student: {stnd.name} removed successfully.")
                return
        print(f"Student with ID: {student_id} Not Found!")

    
    def __str__(self):
        if not self.students:
            return "College has no students enrolled yet."
        return "College Students:\n" + "\n".join(str(stnd) for stnd in self.students)
