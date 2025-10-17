### Customer page
# from account import Account

class Customer:
    def __init__(self, customer_id, name, pin, account):
        self.customer_id = customer_id
        self.name = name
        self.pin = pin
        self.account = account

    def __str__(self):
        return (
            f"CustomerID:{self.customer_id}, Name:{self.name}, "
            f"Balance:{self.account.balance}, AccountNo:{self.account.acc_no}"
        )

# a1=Account(acc_no="12147", customer_id="101", balance=0, transactions=None)
# c1=Customer(customer_id="101", name="Yuvraj", pin="1122", account=a1)
# print(c1)
# print(c1.account.transactions)