from myBook import MyBooks

if __name__ == "__main__":
    bid = "ISBN-101"
    details = {"name": "Thermodynamics", "price": 360, "author": "RS Kurmi"}
    MyBooks.addBook(bid, details)

    bid = "ISBN-102"
    details = {"name": "Fluid Mehcanics", "price": 820, "author": "RK Bansal"}
    MyBooks.addBook(bid, details)

    bid = "ISBN-103"
    details = {"name": "Heat and mass", "price": 470, "author": " Devanad"}
    MyBooks.addBook(bid, details)

    bid = "ISBN-104"
    details = {"name": "Refrigeration ", "price": 280, "author": "AA Arora"}
    MyBooks.addBook(bid, details)

    print("-------------------------------------------------------------------------------")
    MyBooks.displayAllBooks()
    print("-------------------------------------------------------------------------------")
    data=MyBooks.searchBookById(bid)
    print(f"Search result for-{bid}: {data}")

    print("-------------------------------------------------------------------------------")
    MyBooks.deleteBookById(bid)
