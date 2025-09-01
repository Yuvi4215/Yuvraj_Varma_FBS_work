### WAP to print factorial of a number .

num = int(input("Enter the number ::"))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(f"Factorial :: {factorial}")