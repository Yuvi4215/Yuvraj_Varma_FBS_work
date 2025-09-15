# ------------------ Fibonacci with Recursion ------------------

#  Print first n Fibonacci numbers recursively
def fibonacciRecursive(n, a=0, b=1, count=0):

    if count == n:
        return False
    print(a, end=" ")
    fibonacciRecursive(n, b, a + b, count + 1)


#  Print Fibonacci numbers in given range recursively
def fibonacciRangeRecursive(start, end, a=0, b=1):

    if a > end:   # stop when exceeded range
        return False
    if a >= start:
        print(a, end=" ")
    fibonacciRangeRecursive(start, end, b, a + b)


# ---- Test ----
print("-------------------first fibonacci by Recursion---------------------")
num=int(input("Enter count of fibonacci numbers : "))
print(f"First {num} fibonacci numbers :")
fibonacciRecursive(num)

print("\n\n-------------------fibonacci in range by Recursion---------------------")
start=int(input("Enter start of range : "))
end=int(input("Enter end of range : "))
print(f"Fibonacci numbers between {start} and {end} (Loop):")
fibonacciRangeRecursive(start, end)
