### series

n = int(input("Enter the number :: "))
sum = 0
factorial = 1
for i in range(1, n + 1):
    factorial = 1
    for j in range(2, i + 1):
        factorial *= j
    sum = sum + (i / factorial)
    print(f"iteration-{i} and  sum:: {sum}")
