### Write a program to check if the given number is positive or negative.

#Take number input from user
num=int(input("Enter number :: "))

#Perform if else operation to find type of number
if(num==0):
    print(f"{num} is Neutral number.")
elif(num>0):
    print(f"{num} is Positive number.")
else:
    print(f"{num} is Negative number.")
