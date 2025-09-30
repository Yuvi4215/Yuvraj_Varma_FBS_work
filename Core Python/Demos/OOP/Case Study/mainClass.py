### Case Study- Employee management system
from employeManage import EmployeeMethods


def empLogin():
    user_id = "user"
    password = "1234"
    id = input("Enter user ID : ")
    pswd = input("Enter Password : ")
    if id == user_id and password == pswd:
        # if True:
        flag = True
        while flag:
            print(
                f"""
Select Operation.
    1. Add Employee
    2. Update Employee Detailes
    3. Delete Employee
    4. Search Employee by ID
    5. List all Employees
    6. Exit
"""
            )
            choice = input("Enter the choice : ")
            if choice == "1":
                EmployeeMethods.addEmp()
            elif choice == "2":
                EmployeeMethods.updateEmp()
            elif choice == "3":
                EmployeeMethods.deleteEmp()
            elif choice == "4":
                EmployeeMethods.searchEmp()
            elif choice == "5":
                EmployeeMethods.showAllEmp()
            elif choice == "6":
                # print("flag-", flag)
                flag = False
                # print("flag-", flag)
            else:
                "-----------!!!Invalid choice!!!-----------\nEnter correct choice."

    else:
        print("-----------!!! Worning !!!-----------\nUser Id or Password is wrong.\n")


print(
    """
'|| '||'  '|' '||''''|  '||'        ..|'''.|  ..|''||   '||    ||' '||''''|  
 '|. '|.  .'   ||  .     ||       .|'     '  .|'    ||   |||  |||   ||  .    
  ||  ||  |    ||''|     ||       ||         ||      ||  |'|..'||   ||''|    
   ||| |||     ||        ||       '|.      . '|.     ||  | '|' ||   ||       
    |   |     .||.....| .||.....|  ''|....'   ''|...|'  .|. | .||. .||.....|     
"""
)

flag = True
worn = 0
while flag:
    print(("Enter your Choice.\n    1. Login\n    2. Exit"))
    choice = input("Choice : ")
    if choice == "1":
        empLogin()
    elif choice == "2":
        flag = False
        print("Program Ended sucsefully.")
    else:
        worn += 1
        if worn < 3:
            print(
                f"\n!!! Worning :wrong-input!!!\nAttempt-{worn} out of 3, Please enter rignt coice:\n"
            )
        else:
            flag = False
            print("You Have crossed 3rd Attempt. Please start again!")
