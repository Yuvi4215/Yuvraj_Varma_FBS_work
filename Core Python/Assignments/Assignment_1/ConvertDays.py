## Write a program to convert days into years, weeks and days.

# Take days value from user 
days= int(input('Enter days you want to convert :: '))

#Calculate number of years, weeks and days
years=days//365
days=days%365

# find weeks remain
weeks=days//7
days=days%7

# Display results 
print(f'The years :{years} , weeks :{weeks} , days{days}')