# Fibonacci Series up to n terms
num = int(input("Enter the number :: "))

if num < 2:
    print("Need at least 2 terms to start series.")
else:
    first, second = 0, 1
    print(first, second, end=" ")
    for _ in range(num - 2):
        third = first + second
        print(third, end=" ")
        first, second = second, third