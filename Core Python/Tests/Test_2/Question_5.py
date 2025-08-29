### Question5

# take 5 user input values of cost of product
p1 = float(input("Enter the cost for Product 1 :: "))
p2 = float(input("Enter the cost for Product 2 :: "))
p3 = float(input("Enter the cost for Product 3 :: "))
p4 = float(input("Enter the cost for Product 4 :: "))
p5 = float(input("Enter the cost for Product 5 :: "))

# Total bill calculation
total_bill = 1.18 * (p1 + p2 + p3 + p4 + p5)

# Display the results
print(f"Total bill including 18% GST :: {total_bill}")
