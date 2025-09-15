# ------------------ Fibonacci with Loops ------------------

#  Print first n Fibonacci numbers
def fibonacciLoop(n):

    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


#  Print Fibonacci numbers in given range [start, end]
def fibonacciRangeLoop(start, end):
 
    a, b = 0, 1
    while a <= end:
        if a >= start:
            print(a, end=" ")
        a, b = b, a + b
    print()


print("-------------------first fibonacci by loop---------------------")
num=int(input("Enter count of fibonacci numbers : "))
print(f"First {num} fibonacci numbers :")
fibonacciLoop(num)


print("-------------------fibonacci in range by loop---------------------")
start=int(input("Enter start of range : "))
end=int(input("Enter end of range : "))
print(f"Fibonacci numbers between {start} and {end} (Loop):")
fibonacciRangeLoop(start, end)
