### Write a program find reverse of a number


def calculateReverse(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    return reverse_num


num = int(input("Enter the number: "))
result = calculateReverse(num)
print(f"Reverse of {num} is: {result}")
