### Write a program to print prime numbers between 1 to 100.
count = 100

print("--------------------Result--------------------")
for num in range(2, 101):
    for divisor in range(2, num):
        if num % divisor == 0:
            break
    else:
        print(num, end=" ")