### Write a program to print Fibonacci series using recursion.

def printFibonacci(count, a, b):
    if count>0:
        c=a+b
        print(c, end=" ")
        printFibonacci(count-1, b, c)

num= int(input("Enter count of number :: "))
printFibonacci(num,-1,1)