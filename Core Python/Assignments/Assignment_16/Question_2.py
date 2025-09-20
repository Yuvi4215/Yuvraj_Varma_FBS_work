### 2.Create a class Product with members as pid,pname,price and quantity .
# Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowProduct
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.


class Product:
    discount = 20

    def __init__(self, pid="Product-default", pname="Default", price=100, quantity=10):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        self.total = (price - (Product.discount * price) / 100) * quantity

    def showProduct(self):
        print(
            f"""
Product Id       : {self.pid}
Product Name     : {self.pname}
Product Price    : {self.price}
Product Quantity : {self.quantity}
-----------------------------------------
Product Total    : {self.total:.2f}
-----------------------------------------\n
"""
        )

    def __del__(self):
        print("__del__() method called. ")

    @staticmethod
    def getDiscount():
        print("-----------------------------------------")
        print(f"Discount  ::  {Product.discount}%")
        print("-----------------------------------------\n\n")


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
Product.getDiscount()