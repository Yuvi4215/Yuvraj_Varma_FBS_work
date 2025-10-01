### Account class for customer


class Account:
    def __init__(self, acc_no, customer_id, balance=0, transactions=None):
        self.acc_no = acc_no
        self.customer_id = customer_id
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited:{amount}")
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew:{amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")
            return True
        else:
            print("Insufficient funds or invalid amount")
            return False

    def __str__(self):
        return (
            f"AccountNo:{self.acc_no}, Balance:{self.balance}, "
            f"Transactions:{self.transactions[-5:]}"
        )
 
    
a1=Account(acc_no="12147", customer_id="101", balance=0, transactions=None)
print(a1)
print(a1.customer_id)