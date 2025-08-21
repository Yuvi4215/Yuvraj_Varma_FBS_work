## Write a program Program to Find the Roots of a Quadratic Equation

# Take values of a,b and c for ax^2 + bx + c
a=float(input('Enter value of a :: '))
b=float(input('Enter value of b :: '))
c=float(input('Enter value of c :: '))

#calculate Discrimnant using a, b, c
d=((b**2) -(4*a*c) )**.05

#calculate two roots 
r1= (-b+d)/(2*a)
r2= (-b-d)/(2*a)

# Display result
print(f'The first root is::{r1} and second root is::{r2}')