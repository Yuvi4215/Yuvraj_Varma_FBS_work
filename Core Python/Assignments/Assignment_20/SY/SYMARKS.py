

class SYMARKS:
    
    
    def __init__(self, computer_total, maths_total, electronics_total):
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronics_total = electronics_total
    
    def __str__(self):
        return f"{self.computer_total}, {self.maths_total}, {self.electronics_total}"

if __name__=="__main__":
    sy=SYMARKS(89,87,99)
    print(sy)