### Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

print("--------------------Start--------------------")
student_count = int(input("Enter number of students ::"))
classroom_avg = 0.0
for i in range(1, student_count + 1):
    m1 = int(input(f"Enter subject 1 mark for student with roll number {i} :: "))
    m2 = int(input(f"Enter subject 2 mark for student with roll number {i} :: "))
    m3 = int(input(f"Enter subject 3 mark for student with roll number {i} :: "))
    m4 = int(input(f"Enter subject 4 mark for student with roll number {i} :: "))
    m5 = int(input(f"Enter subject 5 mark for student with roll number {i} :: "))
    print("-------------calculation--------------")
    percentage = (m1 + m2 + m3 + m4 + m5) / 5
    classroom_avg = ((classroom_avg * (i - 1) + percentage)) / i
    print(f"Student-{i} ::{percentage }%")
    print(f"Classroom avg % for-{i} students ::{classroom_avg }%")
    print("-------------Next student--------------")