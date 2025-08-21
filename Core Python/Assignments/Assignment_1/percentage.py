## Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Take subject marks from user as input
sub1=int(input('Enter marks of subject 1 :: '))
sub2=int(input('Enter marks of subject 2 :: '))
sub3=int(input('Enter marks of subject 3 :: '))
sub4=int(input('Enter marks of subject 4 :: '))
sub5=int(input('Enter marks of subject 5 :: '))

# Calculate the percentage 
perc= ((sub1+sub2+sub3+sub4+sub5)/500)*100

# Display the results
print(f'The percentage calculated is :: {perc}%')