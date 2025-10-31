class MyBooks:
    data = {}

    @staticmethod
    def addBook(bid, details):
        MyBooks.data[bid] = details
        print(f"Book added with : {bid}")

    @staticmethod
    def deleteBookById(bid):
        del MyBooks.data[bid]
        print(f"Book deleted with : {bid}")

    @staticmethod
    def displayAllBooks():
        print("BID               Name          Price       Author")
        for key,ele in MyBooks.data.items():
            print(key, end="\t")
            for val in ele.values():
                print(val, end="\t")
            print()

    @staticmethod
    def searchBookById(bid):
        return MyBooks.data.get(bid, "Not Available")
