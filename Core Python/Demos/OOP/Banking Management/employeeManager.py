### Employee management Methods
from customerManager import CustomerManager
class EmployeeManager:
    employees = {"cashier":"1234", "manager":"1111",}  # {emp_id: Employee object}

    def login():
        emp_id=input("Enter user ID : ")
        password=input("Enter Password : ")
        if emp_id in EmployeeManager.employees:
            if password== EmployeeManager.employees[emp_id]:
                print("==== Employee Logged in Succesfully. ====")
                attempt=0
                flag=True
                while flag:
                    print(f"""\n==== Welcome mr/ms {emp_id} to Console Bank ====
        1. View all Transactions
        2. View Total Transaction Amount
        3. View All Customers
        4. Exit""")
                    choice = input("Choice : ") 
                    if choice == "1":
                        EmployeeManager.viewAllTransactions()
                    elif choice == "2":
                        EmployeeManager.viewTotalTransactionAmount()
                    elif choice == "3":
                        EmployeeManager.viewAllCustomers()
                    elif choice == "4":
                        print("====!!! Exiting... Goodbye !!!====")
                        flag=False
                    else:
                        attempt+=1
                        if attempt>2:
                            print("====!!! You have reached Attempt limit !!!====")
                            print("====!!! BACK TO LOGIN MENU !!!====")
                            flag=False
                        else:
                            print(f"!!! Attempt {attempt}, out of 3") 
                            print("==== Invalid choice, try again ====")
            else:
                print("==== Invalid User/Password Try again ====")
        else:
            print("==== Invalid User/Password Try again ====")

    @staticmethod
    def viewAllTransactions():
        print("\n=== All Transactions ===")
        for cust_id, customer in CustomerManager.customers.items():
            print(f"\nCustomer: {customer.name} (ID: {cust_id})")
            if customer.account.transactions:
                for txn in customer.account.transactions:
                    print(f"   - {txn}")
            else:
                print("   No transactions found.")

    @staticmethod
    def viewTotalTransactionAmount():
        print("\n=== Total Transaction Amount ===")
        total = 0
        for cust_id, customer in CustomerManager.customers.items():
            for txn in customer.account.transactions:
                if txn.startswith("Deposited:"):
                    total += float(txn.split(":")[1])
                elif txn.startswith("Withdrew:"):
                    total += float(txn.split(":")[1])
        print(f"Total transaction volume across all customers = {total}")

    @staticmethod
    def viewAllCustomers():
        print("\n=== All Customers ===")
        for cust_id, customer in CustomerManager.customers.items():
            print(customer)  # uses Customer.__str__()
