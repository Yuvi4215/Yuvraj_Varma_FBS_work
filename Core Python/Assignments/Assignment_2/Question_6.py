### Write a program to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

# Take Basic Salary amount from user
Basic_salary=float(input('Enter Basic Salary in LPA :: '))

# Perform calculations
total_salary=(1.37*Basic_salary)

# Display the result
print(f'Finally Total Salary amount is ::{total_salary}.')