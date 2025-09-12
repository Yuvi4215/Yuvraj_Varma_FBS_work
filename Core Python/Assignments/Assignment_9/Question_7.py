### Write a program to find sum of digits using recursion.

def sumOfDigit(num):
    if num<10:
        return num
    
    return num%10 +sumOfDigit(num//10)

num=int(input("Enter the number :: "))

print(f"Sum of Digit :: {sumOfDigit(num)}")