from cust_exception import TVException

class Television:
    def __init__(self):
        self.model = 0
        self.screen = 0
        self.price = 0

    def getData(self):
        try:
            m = int(input("Enter model number: "))
            s = int(input("Enter screen size: "))
            p = float(input("Enter price: "))
            TVException().validate(m, s, p)
            self.model = m
            self.screen = s
            self.price = p
        except TVException:
            self.model = 0
            self.screen = 0
            self.price = 0
            print("Invalid Input. Data reset to zero.")

    def display(self):
        print("Model:", self.model)
        print("Screen Size:", self.screen)
        print("Price:", self.price)

def main():
        t = Television()
        t.getData()
        t.display()
if __name__=="__main__":
     main()
