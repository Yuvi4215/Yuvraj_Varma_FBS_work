## Write a program to enter P, T, R and calculate simple Interest.

# Take values of principal amount-P, Time-T and Rate of Interest-R
p=int(input('Enter the Principal Amount :: '))
r=int(input('Enter the Rate of Interest in % :: '))
t=int(input('Enter the Years of replayment :: '))

#calculate Simple Interest using formula
simple_interest=(p*r*t)/100

# Display result
print(f'The Simple interest calculated is :: {simple_interest}')