## Write a program to enter base and height of a triangle and find its area.

# Take Height and Base values from user
height=float(input('Enter Height of triagle :: '))
base=float(input('Enter Base of triagle :: '))

#Calculate the area of triangle
area = 0.5*base*height

# Display Result
print(f'The area of the triangle is : {area}')