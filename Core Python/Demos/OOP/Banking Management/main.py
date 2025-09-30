###
from employeeManager import EmployeeManager
from customerManager import CustomerManager


def run():
    attempt = 0
    flag = True
    while flag:
        print(
            """\n==== Welcome to Console Bank ====
        1. Customer
        2. Employee
        3. Exit"""
        )
        choice = input("Choice : ")
        if choice == "1":
            customerMenu()
        elif choice == "2":
            employeeMenu()
        elif choice == "3":
            print("====!!! Exiting... Goodbye !!!====")
            flag = False
        else:
            attempt += 1
            if attempt > 2:
                print("====!!! You have reached Attempt limit !!!====")
                flag = False
            else:
                print(f"!!! Attempt {attempt}, out of 3")
                print("==== Invalid choice, try again ====")


def customerMenu():
    flag = True
    attempt = 0
    while flag:
        print(
            """\n---- Customer Menu ----
        1. Register
        2. Login
        3. Back"""
        )
        choice = input("Choice : ")
        if choice == "1":
            CustomerManager.createNewAccount()
        elif choice == "2":
            CustomerManager.login()
        elif choice == "3":
            print("====!!! Previous Menu !!!====")
            flag = False
        else:
            attempt += 1
            if attempt > 2:
                print("====!!! You have reached Attempt limit !!!====")
                flag = False
            else:
                print(f"!!! Attempt {attempt}, out of 3")
                print("==== Invalid choice, try again ====")


def employeeMenu():
    flag = True
    attempt = 0
    while flag:
        print(
            """\n---- Employee Menu ----
        1. Login
        2. Back"""
        )
        choice = input("Choice : ")
        if choice == "1":
            EmployeeManager.login()
        elif choice == "2":
            print("====!!! Previous Menu !!!====")
            flag = False
        else:
            attempt += 1
            if attempt > 2:
                print("====!!! You have reached Attempt limit !!!====")
                print("====!!! BACK TO MAIN MENU !!!====")
                flag = False
            else:
                print(f"!!! Attempt {attempt}, out of 3")
                print("==== Invalid choice, try again ====")


run()
# flag=True
# attempt=0
# while flag:

#     print("""Welcome to banking portal
#         Choose from follwing option :
#             1. Customer page
#             2. Employee page
#             3. Exit
#         """)
#     choice=input("Choice : ")
#     if choice=="1":
#         pass
#     elif choice=="2":
#         pass
#     elif choice=="3":
#         pass
#     else:
#         attempt+=1
#         if attempt>2:
#             print("---------------!!! You have reached Attempt limit !!!---------------")
#             flag=False
#         else:
#             print(f"Attempt {attempt}, out of 3")
