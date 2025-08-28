### Write a program to Find the sum of three-digit number.

# Take the three digit number from user
number=int(input('Enter the Number :: '))

sum=0
while(number>0):
    digit=number%10
    number=number//10
    sum+=digit

# Display the result
print(f'Finally the Sum of digits is ::{sum}')