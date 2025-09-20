### 1.Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:
    count = 0

    def __init__(
        self, bid="Defalut-Bid", bname="Defalut-Name", price=0, author="Defalut-Author"
    ):
        Book.count += 1
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showBook(self):
        print(
            f"""
-----------------------------------------
Book Id     : {self.bid}
Book Name   : {self.bname}
Book Price  : {self.price}
Book Author : {self.author}
-----------------------------------------\n
"""
        )

    def __del__(self):
        print("__del__() method called. ")

    @staticmethod
    def getCount():
        print("-----------------------------------------")
        print("Total book objects count :: ", Book.count)
        print("-----------------------------------------\n\n")


b1 = Book()  # values by- default values
b2 = Book("JDCFN", "Thor", 876, "kevin")
b3 = Book("JFOIM", "Iron-man", 921, "kevin")
b4 = Book("PWJHG", "Hulk", 185, "kevin")
b5 = Book("OWDFG", "Spider-man", 752, "kevin")

b1.showBook()
b2.showBook()
b3.showBook()
b4.showBook()
b5.showBook()

Book.getCount()