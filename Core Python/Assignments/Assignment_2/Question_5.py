### Write a program to calculate selling price of book based on cost price and discount.

# Take Cost price and discount values from user
cost=float(input('Enter Cost of Book :: '))
discount=float(input('Enter Discount on Book in % :: '))

# Perform Calculation for selling price
selling_price=cost -(cost*discount)/100


# Display the result
print(f'Finally Selling Price ::{selling_price}.')