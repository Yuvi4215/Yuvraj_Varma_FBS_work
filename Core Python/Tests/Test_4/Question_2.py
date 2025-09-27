### 2. Write a program to find factorial of given number using recursion


def getFactorial(num):
    if num == 1:
        return 1
    return num * getFactorial(num - 1)


number = int(input("Enter the number :"))
fact = getFactorial(number)
print(fact)