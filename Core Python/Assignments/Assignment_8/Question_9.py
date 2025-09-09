### write a program to check if enterd number is palindrome or not


def checkPalindrome(num):
    temp = num

    new_num = 0
    while temp > 0:
        digit = temp % 10  # last digit
        new_num = new_num * 10 + digit
        temp = temp // 10

    return new_num == num

num= int(input("Enter number :: "))

if checkPalindrome(num):
    print("number is- palindrome")
else:
    print("number is- not palindrome")
