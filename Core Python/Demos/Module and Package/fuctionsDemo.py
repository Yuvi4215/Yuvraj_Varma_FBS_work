### functions file to hold multiple functions

# 1. Fucntion addition
def add(x,y):
    return x+y

# 2. Fuction Factorial
def fact(num):
    fact=1
    for ele in range(2, num+1):
        fact*=ele
    return fact

# 3. Fuction check if it is even
def isEven(num):
    return num%2==0

if __name__=="__main__":
    print(add(14,41))
    print(fact(4))
    print(isEven(47))