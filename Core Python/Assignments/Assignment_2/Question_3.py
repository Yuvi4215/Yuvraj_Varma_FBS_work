### Write a program to Convert distant given in feet and inches into meter and centimeter.

# Take feet and inches values from user
feet=float(input('Enter the Feet value :: '))
inches=float(input('Enter inch value :: '))

# Perform convsion
milimeter= (feet*12*25.4)+(inches*25.4)

# Display the result
print(f'Finally the meter value ::{milimeter/1000} and centimeter ::{milimeter/10}')