## Write a program to enter P, T, R and calculate Compound Interest.

# Take values of principal amount-P, Time-T and Rate of Interest-R
p=int(input('Enter the Principal Amount :: '))
r=int(input('Enter the Rate of Interest in % :: '))
t=int(input('Enter the Years of replayment :: '))

#calculate Simple Interest using formula
Compound_interest=p*(1+(r/100))**t -p

# Display result
print(f'The Compound interest calculated is :: {Compound_interest}')