### Write a program to to swap two numbers without using third variable.

# Take two number values from user
num1=int(input('Enter the first number :: '))
num2=int(input('Enter the second number :: '))

# Perform swapping using 3rd variable
num1=num1+num2
num2=num1-num2
num1=num1-num2


# Display the result
print(f'Finally First number is ::{num1} and Second Number is ::{num2}')