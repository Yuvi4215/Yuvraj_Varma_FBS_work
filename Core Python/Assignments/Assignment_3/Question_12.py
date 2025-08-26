### Write a program to check if given 3 digit number is a palindrome or not.

# Take 3 digit number from user
num=int(input("Enter the number ::"))

# sepereate each digit 
last=num%10
num=num//10

middle=num%10
num=num//10

first=num%10
num=num//10

print(f"first : {first}, middle : {middle}, last : {last}")

if (first==last):
    print(f"Digit is a palindrome.")
else:
    print(f"Digit is not a palindrome ")