basic = int(input("Enter the basic salary ::"))
salary = 0
if basic < 20000:
    salary = 1.37 * basic
else:
    salary = 1.53 * basic

print("salary is ::", salary)
