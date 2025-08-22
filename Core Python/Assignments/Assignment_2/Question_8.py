### Write a program to swap two numbers using third variable.

# Take two number values from user
num1=int(input('Enter the first number :: '))
num2=int(input('Enter the second number :: '))

# Perform swapping using 3rd variable
temp=num1
num1=num2
num2=temp


# Display the result
print(f'Finally First number is ::{num1} and Second Number is ::{num2}')