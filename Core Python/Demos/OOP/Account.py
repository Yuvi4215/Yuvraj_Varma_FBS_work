### Account

class Account:
    branch_name="BOB- Solapur, main"
    ifcs_code="BOB00002"

    def __init__(self, name, ac_no, bal ):
        self.holder_name=name
        self.account_no=ac_no
        self.balance=bal

    def displayResult(self):
        print(f"HOLDER NAME :: {self.holder_name }")
        print(f"ACCOUNT NUMBER :: {self.account_no }")
        print(f"BALANCE :: { self.balance}")
        print(f"BRANCH NAME :: {Account.branch_name }")
        print(f"IFSC CODE :: {Account.ifcs_code }")


a1=Account("Thor", 1212, 159)
a1.displayResult()
print("---------------------------------\n\n")
a2=Account("Wonda", 1213, 697)
a2.displayResult()