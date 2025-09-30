### Customer page

class Customer: 
    def __init__(self, customer_id, name, pin, account):
        self.customer_id = customer_id
        self.name = name
        self.pin = pin
        self.account = account

    def __str__(self):
        return (f"CustomerID:{self.customer_id}, Name:{self.name}, "
                f"Balance:{self.account.balance}, AccountNo:{self.account.acc_no}")

