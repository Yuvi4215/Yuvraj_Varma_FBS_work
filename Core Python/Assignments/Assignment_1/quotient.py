# Write the Program to find quotient and remainder of two numbers.

# Take Divident and Divisor from user as input
num1= int(input('Enter Divident value :: '))
num2= int(input('Enter Divisor value :: '))

# Perform calculation for quotient and remainder
quotient=num1//num2

remainder=num1%num2

#Display Results
print(f"""Quotient ::{quotient} 
       Reminder is ::{remainder}""")