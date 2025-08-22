### Write a program to Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

#Take input from user for celsius
celsius=float(input('Enter the Celsius reading :: '))

#convert to fahrenheit
fahrenheit=(celsius*9)/5 +32

#Display the result
print(f'The converted Fahrenheit reading is :: {fahrenheit}')