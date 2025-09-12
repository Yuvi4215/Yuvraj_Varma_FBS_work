### Write a program to check whether a number is prime or not using recursion.


def isPrimeNumber(num, index=2):
    if num <= 1:
        return False
    if index > int(num**0.5):
        return True
    if num % index == 0:
        return False
    return isPrimeNumber(num, index + 1)



num = int(input("Enter the number :: "))
if isPrimeNumber(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")