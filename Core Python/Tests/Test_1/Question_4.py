# Question 4

# Take input from User for wall and cost for interior and exterior
area =float(input('Considering both rooms are Squre and of same size, please inter area of of any wall :: '))
interior=float(input('Enter the cost per unit area for Interior:: '))
exterior=float(input('Enter the cost per unit area for Exterior:: '))

# calculate the total cost for painting
total_interior_area=(8*area)
total_exterior_area=(7*area)

interior_cost=(total_interior_area*interior)
exterior_cost=(total_exterior_area*exterior)


#display the reslut
print(f'Total cost of painting is :: {interior_cost+exterior_cost}')