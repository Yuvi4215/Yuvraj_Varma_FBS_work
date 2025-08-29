### Write a program to reverse three-digit number.

# Take the three digit number from user
number = int(input("Enter the Number :: "))
reverse = 0

# perform revering operation
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# Display the result
print(f"Finally Reversed digits is ::{reverse}")