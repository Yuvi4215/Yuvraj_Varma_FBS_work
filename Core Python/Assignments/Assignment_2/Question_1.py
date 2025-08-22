### Write a program to Convert the time entered in hh,min and sec into seconds.

#Take user input for HH, MM and SS from user
hour=int(input('Enter Hours :: '))
min=int(input('Enter Minutes :: '))
seconds=int(input('Enter Seconds :: '))

#calculate the tatal seconds
seconds= (hour*3600)+(min*60)+seconds

# Display the results
print(f'The total seconds are :: {seconds}')