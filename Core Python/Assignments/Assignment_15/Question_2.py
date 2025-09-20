### 2. Create a class Product with members as pid,pname,price and quantity .
# Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowProduct


class Product:

    def __init__(self, pid="Product-default", pname="Default", price=100, quantity=10):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print(
            f"""
-----------------------------------------
Product Id       : {self.pid}
Product Name     : {self.pname}
Product Price    : {self.price}
Product Quantity : {self.quantity}
-----------------------------------------
"""
        )

    def __del__(self):
        print("__del__() method called. ")

p1 = Product()  # values by- default values
p2 = Product("D-CFN", "Book", 876, 120)
p3 = Product("D-KSS", "Drafter", 256, 11)
p4 = Product("D-IRD", "Box", 123, 50)
p5 = Product("D-PKJ", "Pen-v7", 75, 4)

p1.showProduct()
p2.showProduct()
p3.showProduct()
p4.showProduct()
p5.showProduct()