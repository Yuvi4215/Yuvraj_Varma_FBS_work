### Write a program to find factorial using recursion.


def getFactrorial(num):
    if num <= 0:
        return 1
    return num * getFactrorial(num - 1)

num=int(input("Enter the value :: "))
print(f"Factrorial for {num} is :: {getFactrorial(num)} ")