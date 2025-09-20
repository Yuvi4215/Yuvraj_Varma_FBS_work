### 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .
# Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowShirts
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.


class Shirts:
    size_increment = {"small": 0, "medium": 10, "large": 20, "xlarge": 30}

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
        self.size = size.lower()
        self.base_price = price
        self.price = self.calculatePrice(self.size, price)

    def showShirts(self):
        print(
            f"""
-----------------------------------------
Shirt ID        : {self.sid}
Shirt Name      : {self.sname}
Shirt Type      : {self.stype}
Shirt Size      : {self.size}
Shirt Base Price: {self.base_price}
-----------------------------------------
Shirt Price     : {self.price:.2f}
-----------------------------------------
        """
        )

    def __del__(self):
        print("Destructor Called :: ")

    @staticmethod
    def calculatePrice(size, price):
        increment = Shirts.size_increment.get(size, 40)
        return price * (1 + increment / 100)


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