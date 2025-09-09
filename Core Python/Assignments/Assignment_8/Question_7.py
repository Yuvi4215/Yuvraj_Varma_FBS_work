### Write a program to find sum of digits of a number.

def calculateDigitSum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum


num = int(input("Enter the number: "))
result = calculateDigitSum(num)
print(f"Sum of digits of {num} is: {result}")
