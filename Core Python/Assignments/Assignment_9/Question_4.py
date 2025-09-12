### Write a program to find sum of n numbers using recursion.
def getSum(num):
    if num < 1:
        return 0
    return num + getSum(num - 1)


# num=9
num = int(input("Enter the n value :: "))
print(f"Sum of {num} digit number :: {getSum(num)}")