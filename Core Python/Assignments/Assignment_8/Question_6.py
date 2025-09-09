### Write a program to print following Fibonacci series using function


def printFibinacci(num):
    
    a,b= 0,1
    print(b, end=" ")
    for i in range(1, num):
        c= a+b
        print(c, end=" ")
        a,b=b,c

num= int(input("Enter numbers count ::"))
printFibinacci(num)