### class with Static methods 
from dev import Dev
from hr import HR
from admin import Admin
from prettytable import PrettyTable


class EmployeeMethods:
    # emp_details = {}
    emp_details = {
        "101": "101, Yuvraj, 69000.0, 91080.0, S/W Developer",
        "102": "102, Deepak, 52333.0, 66147.92, HR",
        "103": "103, Urvashi, 12000.0, 15960.0, Admin",
        "201": "201, Pallavi, 47555.0, 61518.2, HR",
    }

    def addEmp():
        id = input("Enter the Employee ID : ")
        name = input("Enter the Employee Name : ")
        basic_sal = float(input("Enter the Basic Salary : "))
        flag = True
        while flag:
            print("Select the department:\n1. S/W Developer\n2. HR\n3. Admin")
            choice = input("Choice : ")
            if choice == "1":
                flag = False
                bonous = float(input("------------- Enter the `Bonous` Amount : "))
                d1 = Dev(id, name, basic_sal, bonous)
                e_data = str(d1)
                EmployeeMethods.emp_details[id] = e_data
                # print(e_data)
                print(
                    f"-----------------Emplyee detailes added with ID : {id}-----------------"
                )
                print(f"Dictionary :: {EmployeeMethods.emp_details}")

            elif choice == "2":
                flag = False
                comm = float(input("------------- Enter the `Commision` Amount : "))
                h1 = HR(id, name, basic_sal, comm)
                e_data = str(h1)
                EmployeeMethods.emp_details[id] = e_data
                # print(e_data)
                print(
                    f"-----------------Emplyee detailes added with ID : {id}-----------------"
                )
                print(f"Dictionary :: {EmployeeMethods.emp_details}")

            elif choice == "3":
                flag = False
                allownce = float(input("------------- Enter the `Allownce` Amount : "))
                a1 = Admin(id, name, basic_sal, allownce)
                e_data = str(a1)
                EmployeeMethods.emp_details[id] = e_data
                # print(e_data)
                print(
                    f"-----------------Emplyee detailes added with ID : {id}-----------------"
                )
                print(f"Dictionary :: {EmployeeMethods.emp_details}")
            else:
                print("-----------!!!Please Enter correct choice!!!-----------")

    def updateEmp():
        id = input("Enter Employee ID you want to Update : ")
        value = EmployeeMethods.emp_details.get(id, "not found")
        if value == "not found":
            print(f"There is no employee with ID : {id}")
        else:
            value = value.split(", ")
            id = value[0]
            name = value[1]
            basic_salary = float(value[2])
            dept = value[4]
            # print(value)
            print(id, name, basic_salary, value[3], dept)

            flag = True
            while flag:
                print("Select which detaile to be updated:\n1. Name\n2. Basic Salary")
                choice = input("Choice :")
                if choice == "1":
                    flag = False
                    name = input("Enter new Name : ")
                    EmployeeMethods.update(id, name, basic_salary, dept)

                elif choice == "2":
                    flag = False
                    basic_salary = float(input("Enter new Total Salary : "))
                    EmployeeMethods.update(id, name, basic_salary, dept)
                else:
                    print("-----------!!!Incorrect Choice!!!-----------")
        
        
        # id=input("Enter Employee ID you want to Update : ")
        # value=EmployeeMethods.emp_details.get(id,"not found")
        # if value=="not found":
        #     print(f"There is no employee with ID : {id}")
        # else:
        #     value=value.split(", ")
        #     id=value[0]
        #     name=value[1]
        #     total_salary=value[3]
        #     dept=value[4]
        #     # print(value)
        #     print(id, name,value[2], total_salary,dept)

        #     flag=True
        #     while flag:
        #         print("Select which detaile to be updated:\n1. Name\n2. Total Salary\n3. Department")
        #         choice=input("Choice :")
        #         if choice=="1":
        #             flag=False
        #             name=input("Enter new Name : ")
        #             EmployeeMethods.emp_details[id]=f"{id}, {name}, {value[2]}, {total_salary}, {dept}"

        #         elif choice=="2":
        #             flag=False
        #             total_salary=float(input("Enter new Total Salary : "))
        #             EmployeeMethods.emp_details[id]=f"{id}, {name}, {value[2]}, {total_salary}, {dept}"
        #             pass
        #         elif choice=="3":
        #             flag=False
        #             dept=input("Enter new Department :")
        #             EmployeeMethods.emp_details[id]=f"{id}, {name}, {value[2]}, {total_salary}, {dept}"
        #             pass
        #         else:
        #             print("-----------!!!Incorrect Choice!!!-----------")

    def update(id, name, basic_salary, dept):
        if dept == "S/W Developer":
            d1 = Dev(id, name, basic_salary)
            e_data = str(d1)
            EmployeeMethods.emp_details[id] = e_data
            print("DEV ", e_data)
        elif dept == "HR":
            h1 = HR(id, name, basic_salary)
            e_data = str(h1)
            EmployeeMethods.emp_details[id] = e_data
            print("HR ", e_data)
        else:
            a1 = Dev(id, name, basic_salary)
            e_data = str(a1)
            EmployeeMethods.emp_details[id] = e_data
            print("ADMIN ", e_data)



    def deleteEmp():
        id = input("Enter Employee ID you want to Delete : ")
        value = EmployeeMethods.emp_details.get(id, "not found")
        if value == "not found":
            print(f"There is no employee with ID : {id}")
        else:
            del EmployeeMethods.emp_details[id]
            print(f"Employee detailes with ID : {id} deleted successfully.")
            print(EmployeeMethods.emp_details)

    def showAllEmp():
        if not EmployeeMethods.emp_details:
            print("There is no Employee Record Found !!!")
        else:
            table= PrettyTable(["ID", "NAME","BASIC","TOTAL","DEPT"])
            for val in EmployeeMethods.emp_details.values():
                words = val.split(", ")
                table.add_row(words)
            print(table)    
            # print("ID\tNAME\t Basic\t  Total\t\tDept")
            # for val in EmployeeMethods.emp_details.values():
                # print(val)
                # table.add_row(val)
                # words = val.split(", ")
            #     for ele in words:
            #         print(ele, end="    ")
            #         print()
            

    def searchEmp():
        id = input("Enter the Employee ID : ")
        value = EmployeeMethods.emp_details.get(id, "not found")
        if value == "not found":
            print(f"There is no employee with ID : {id}")
        else:
            print(f"Employee detailes-")
            table= PrettyTable(["ID", "NAME","BASIC","TOTAL","DEPT"])
            words = value.split(", ")
            table.add_row(words)
            print(table) 
            # words = value.split(", ")
            # for ele in words:
            #     print(ele, end="   ")
            # print()
