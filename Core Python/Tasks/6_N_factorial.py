### WAP to add first N numbers

# Take user Input
num = int(input("Enter Number :: "))
factorial = 1

# factorial using loop
if num < 0:
    # Display result
    print("Undefined value.")
else:
    while num > 1:
        factorial *= num
        num -= 1
    # Display result
    print(f"The factorial is :: {factorial}")
