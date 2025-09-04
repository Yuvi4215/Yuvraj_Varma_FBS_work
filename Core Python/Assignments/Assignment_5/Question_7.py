### Write a program to print first n prime numbers.
first_n = int(input("Enter count of prime number need to be printed :: "))
print("--------------------Result--------------------")
num = 2
count = 0
while True:
    for divisor in range(2, num):
        if num % divisor == 0:
            break
    else:
        count += 1
        print(num, end=" ")
    num += 1

    if count == first_n:
        break