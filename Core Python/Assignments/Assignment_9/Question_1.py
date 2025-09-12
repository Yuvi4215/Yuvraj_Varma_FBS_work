### 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def getFactorial(num):
    if num==1:
        return 1
    return num* getFactorial(num-1)

def getFactSum(num):
    if num==1:
        return 1
    return getFactorial(num)+ getFactSum(num-1)

num=int(input("Enter the number :: "))
print(f"Sum of {num} Factorials is :: {getFactSum(num)}")