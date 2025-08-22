### Write a program to reverse three-digit number.

# Take the three digit number from user
number=int(input('Enter the Number :: '))

# performing digit reverse operation
last=number%10
number=number//10
middle=number%10
number=number//10
first=number%10
reverse_digit=(last*100)+(middle*10)+first

# Display the result
print(f'Finally Reversed digits is ::{reverse_digit}')