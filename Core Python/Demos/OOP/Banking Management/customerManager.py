### Customer management Methods
from customer import Customer
from account import Account


class CustomerManager:
    customers = {
        "101": Customer("101", "Yuvraj", "1122", Account("10110", "101", 0)),
        "102": Customer("102", "Kaviraj", "1122", Account("22014", "102", 0)),
        "103": Customer("103", "Shivraj", "1122", Account("64822", "103", 0)),
    }

    @staticmethod
    def createNewAccount():
        cid = input("Enter new Customer ID: ")
        name = input("Enter Customer Name: ")
        pin = input("Set PIN: ")
        acc_no = input("Enter new Account Number: ")
        if cid not in CustomerManager.customers:
            account = Account(acc_no, cid, 0)
            customer = Customer(cid, name, pin, account)
            CustomerManager.customers[cid] = customer
            print(f"Account created for {name} with ID {cid}")
        else:
            print("====!!! Customer ID already exists !!!====")

    @staticmethod
    def login():
        cstm_id = input("Enter Customer ID: ")
        pin = input("Enter PIN: ")

        customer = CustomerManager.customers.get(cstm_id)
        if customer and customer.pin == pin:
            print(f"Welcome {customer.name}, login successful!")
            CustomerManager.customerMenu(customer)
        else:
            print("====!!! Invalid ID or PIN !!!====")

    @staticmethod
    def customerMenu(customer):
        flag = True
        while flag:
            print(
                f"""\n==== Welcome {customer.name} ====
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Change Pin
    5. Exit"""
            )
            choice = input("Choice: ")
            if choice == "1":
                print(f"Balance: {customer.account.balance}")
            elif choice == "2":
                amt = float(input("Enter deposit amount: "))
                customer.account.deposit(amt)
            elif choice == "3":
                amt = float(input("Enter withdrawal amount: "))
                customer.account.withdraw(amt)
            elif choice == "4":
                CustomerManager.changePin(customer)
            elif choice == "5":
                print("====!!! Logging out... !!!====")
                flag = False
            else:
                print("====!!! Invalid choice !!!====")

    @staticmethod
    def changePin(customer):
        old_pin = input("Enter current PIN: ")
        if old_pin == customer.pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Re-enter new PIN: ")
            if new_pin == confirm_pin:
                customer.pin = new_pin
                print("PIN changed successfully!")
            else:
                print("====!!! PINs do not match. Try again !!!====")
        else:
            print("====!!!Incorrect current PIN. !!!====")


# from account import Account
# from customer import Customer
# class CustomerManager:
#     customers = {
#         "101": Customer("101", "Yuvraj", "1122", Account("10110", "101", 0, [])),
#         "102": Customer("102", "Kaviraj", "1122", Account("22014", "102", 0, [])),
#         "103": Customer("103", "Shivraj", "1122", Account("64822", "103", 0, [])),
#     }


#     def createNewAccount():
#         pass

#     def login():
#         cstm_id=input("Enter Customer ID : ")
#         pin=input("Enter Pin : ")
#         if cstm_id in CustomerManager.customers:
#             pswd=CustomerManager.customers[cstm_id].split(", ")[1].split(":")[1]
#             customer_name=CustomerManager.customers[cstm_id].split(", ")[2].split(":")[1]
#             account_no=CustomerManager.customers[cstm_id].split(", ")[3].split(":")[1]
#             balance=float(CustomerManager.customers[cstm_id].split(", ")[5].split(":")[1])
#             string_list=CustomerManager.customers[cstm_id].split(", ")[6].split(":")[1]   #list
#             transaction=string_list.strip("[]").split(", ")

#             print(pswd)
#             if pin== pswd:
#                 customer = CustomerManager.customers.get(cstm_id)
#                 print("==== Customer Logged in Succesfully. ====")
#                 attempt=0
#                 flag=True
#                 while flag:
#                     print(f"""\n==== Welcome mr/ms {customer_name} to Console Bank ====
#         1. Check Balance
#         2. Deposit Money
#         3. Withdraw Money
#         4. Transfer Money
#         5. Change Pin
#         6. Exit""")
#                     choice = input("Choice : ")
#                     if choice == "1":
#                         CustomerManager.checkBalance(cstm_id)
#                     elif choice == "2":
#                         CustomerManager.depositMoney(cstm_id,pswd,customer_name,account_no,balance,transaction)
#                     elif choice == "3":
#                         CustomerManager.withdrawMoney()
#                     elif choice == "4":
#                         CustomerManager.transfer()
#                     elif choice == "5":
#                         CustomerManager.changePin()
#                     elif choice == "6":
#                         print("====!!! Exiting... Goodbye !!!====")
#                         flag=False
#                     else:
#                         attempt+=1
#                         if attempt>2:
#                             print("====!!! You have reached Attempt limit !!!====")
#                             print("====!!! BACK TO LOGIN MENU !!!====")
#                             flag=False
#                         else:
#                             print(f"!!! Attempt {attempt}, out of 3")
#                             print("==== Invalid choice, try again ====")
#             else:
#                 print("==== Invalid User/Password Try again ====")
#         else:
#             print("==== Invalid User/Password Try again ====")

#     def checkBalance(cstm_id):
#         balance=CustomerManager.customers[cstm_id].split(", ")[5].split(":")[1]
#         print(f"====Balance : {balance}====")

#     def depositMoney(cstm_id,pswd,customer_name,account_no,balance,transaction):
#         amnt=float(input("Enter the Deposit Amount : "))
#         print(balance, amnt)
#         a1= Account(account_no, cstm_id, balance,transaction)
#         a1.deposit(amnt)
#         c1= Customer(cstm_id,customer_name,pswd,a1)
#         print(c1)
#         print(CustomerManager.customers)
#         print(cstm_id)
#         CustomerManager.customers[cstm_id]=str(c1)

#     def withdrawMoney():
#         pass

#     def transfer():
#         pass

#     def changePin():
#         pass
