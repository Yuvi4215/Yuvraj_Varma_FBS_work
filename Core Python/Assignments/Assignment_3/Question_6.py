### Write a program to calculate profit or loss.

#take user input for cost price and selling price
cost=float(input("Enter the cost price of product :: "))
selling=float(input("Enter the Selling price of Product :: "))

#perform branching 
if(selling>cost):
    print(f"You have made a profit of {(selling-cost)} per product")
elif(selling==cost):
    print(f"You have achived Break-even(No Profit, No Loss).")
else:
    print(f"You have made a Loss of {(cost-selling)} per product")