### Write a program to reverse three-digit number.

# Take the three digit number from user
number=int(input('Enter the Number :: '))
temp="1"
count=len(str(number)) #gives count after coverting into string

while count>0:
    temp+="0"   #streing 100....
    count-=1    # finally count=0

temp=int(temp)  #convert str 100.. into int 100...
while number>0:
    digit=number%10
    number=number//10
    count+=digit*(temp/10)



# Display the result
print(f'Finally Reversed digits is ::{count}')