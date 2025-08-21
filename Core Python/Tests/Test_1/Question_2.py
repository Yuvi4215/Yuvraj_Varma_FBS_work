## Question 2

# Take user input for Principal, rate and time
p=float(input('Enter Principal amount :: '))
r=int(input('Enter the rate of interest in percentage only ::'))
t=int(input('Enter time in years only ::'))

# calculate the principal amount
simple_interest= (p*r*t)/100

# Display the results 
print(f'So the Simple Interest is :: {simple_interest}')
