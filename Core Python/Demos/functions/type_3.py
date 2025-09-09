### without passing parameter and with returning value


def getFactorial():
    fact = 1
    num = int(input("Enter the number :: "))

    for i in range(1, num + 1):
        fact *= i
    return fact


res = getFactorial()
print("Factorial value :: ", res)