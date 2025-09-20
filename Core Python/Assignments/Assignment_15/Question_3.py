### 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).
# Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirts


class Shirts:

    def __init__(
        self,
        sid="Default-AAA",
        sname="Default-Name",
        stype="Default-formal",
        price=600,
        size="small",
    ):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size
        self.price = price

    def showShirts(self):
        print(
            f"""
-----------------------------------------
Shirt ID    : {self.sid}
Shirt Name  : {self.sname}
Shirt Type  : {self.stype}
Shirt Size  : {self.size}
Shirt Price : {self.price}
-----------------------------------------

"""
        )

    def __del__(self):
        print("Destructor Called :: ")



s1 = Shirts()  # Default para Constructor
s2 = Shirts("S101", "Formal Shirt", "formal", 800, "small")
s3 = Shirts("S102", "Casual", "casual", 700, "medium")
s4 = Shirts("S103", "Denim Shirt", "casual", 1200, "large")
s5 = Shirts("S104", "Party Shirt", "partywear", 1000, "xlarge")
s6 = Shirts("S105", "Hoodie", "hoodie", 2000, "xxlarge")


s1.showShirts()
s2.showShirts()
s3.showShirts()
s4.showShirts()
s5.showShirts()
s6.showShirts()
