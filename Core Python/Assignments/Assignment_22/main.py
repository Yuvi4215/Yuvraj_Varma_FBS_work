import os
from emp import Emp


def add_record():
    eid = input("Enter ID: ")
    ename = input("Enter Name: ")
    basic = input("Enter Salary: ")
    e = Emp(eid, ename, basic)
    with open("Core Python/Assignments/Assignment_22/emp.txt", "a") as f:
        f.write(f"{e.eid},{e.ename},{e.basic}\n")


def display_all():
 
    with open("Core Python/Assignments/Assignment_22/emp.txt", "r") as f:
        data = f.readlines()
        if len(data) == 0:
            print("No records")
            return
        for line in data:
            eid, ename, basic = line.strip().split(",")
            print(eid, ename, basic)


def search_record():
 
    eid = input("Enter ID to search: ")
    found = False
    with open("Core Python/Assignments/Assignment_22/emp.txt", "r") as f:
        for line in f:
            eid2, ename, basic = line.strip().split(",")
            if eid2 == eid:
                print(eid2, ename, basic)
                found = True
                break
    if not found:
        print("Not found")


def delete_record():
 
    eid = input("Enter ID to delete: ")
    lines = []
    found = False
    with open("Core Python/Assignments/Assignment_22/emp.txt", "r") as f:
        for line in f:
            if line.split(",")[0] != eid:
                lines.append(line)
            else:
                found = True
    with open("Core Python/Assignments/Assignment_22/emp.txt", "w") as f:
        for line in lines:
            f.write(line)
    print("Deleted" if found else "Not found")


def edit_record():
 
    eid = input("Enter ID to edit: ")
    lines = []
    found = False
    with open("Core Python/Assignments/Assignment_22/emp.txt", "r") as f:
        for line in f:
            id2, name, sal = line.strip().split(",")
            if id2 == eid:
                name = input("Enter new name: ")
                sal = input("Enter new salary: ")
                lines.append(f"{eid},{name},{sal}\n")
                found = True
            else:
                lines.append(line)
    with open("Core Python/Assignments/Assignment_22/emp.txt", "w") as f:
        for line in lines:
            f.write(line)
    print("Updated" if found else "Not found")


flag = True
while flag:
    print(
        """
================== Employee Menu ==================
1. Add Record
2. Search Record
3. Delete Record
4. Edit Record
5. Display All
6. Exit"""
    )
    ch = input("Choice: ")
    if ch == "1":
        add_record()
    elif ch == "2":
        search_record()
    elif ch == "3":
        delete_record()
    elif ch == "4":
        edit_record()
    elif ch == "5":
        display_all()
    elif ch == "6":
        flag = False
    else:
        print("Invalid choice")
