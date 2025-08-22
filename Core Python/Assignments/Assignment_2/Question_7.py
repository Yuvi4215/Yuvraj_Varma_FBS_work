### Write a program to Find the sum of three-digit number.

# Take the three digit number from user
number=int(input('Enter the Number :: '))

# Perform sum of digits
last=number%10
number=number//10
middle=number%10
number=number//10
first=number%10
sum=first+middle+last

# Display the result
print(f'Finally the Sum of digits is ::{sum}')