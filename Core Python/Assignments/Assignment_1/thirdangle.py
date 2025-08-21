## Write a Program to input two angles from user and find third angle of the triangle.

# Take Angle values from user as input
angle1 =int(input('Enter the 1st Angle :: '))
angle2 =int(input('Enter the 2nd Angle :: '))


# Calculate the Third angle 
angle3 = 180- (angle1+angle2)

# Display the results
print(f'The Third Angle calculated is :: {angle3} units')