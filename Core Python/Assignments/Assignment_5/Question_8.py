print("--------------------Start--------------------")
# a. 1! + 2! + 3! + 4! + …..n!
print("a. 1! + 2! + 3! + 4! + …..n!")
num = int(input("Enter the number :: "))
n = num
total = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total += factorial
print("--------------------Result--------------------")
print(f"Sum :: {total}")


# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
print()
print("b. N + N^2 + N^3+N^4 …..+N^N")
n = num
total = 0
for i in range(1, n + 1):
    total += n**i  # <-- Corrected to exponent
print("--------------------Result--------------------")
print(f"Sum :: {total}")


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
print()
print("c. Sum of a geometric series")
n = int(input("Enter the number of terms :: "))
r = 2
# Formula for geometric series sum: (r^n - 1) / (r - 1)
total = (r**n - 1) // (r - 1)
print("--------------------Result--------------------")
print(f"Sum :: {total}")


# d. S = a + a^2 / 2 + a^3 / 3 + …… + a^10 / 10
print()
print("d. S = a + a^2/2 + a^3/3 + …… + a^10/10")
a = int(input("Enter the value of a :: "))
total = 0
for i in range(1, 11):
    total += (a**i) / i
print("--------------------Result--------------------")
print(f"Sum :: {total}")


# e. x - x^2/3 + x^3/5 - x^4/7 + …. to n terms
print()
print("e. x - x^2/3 + x^3/5 - x^4/7 + …. to n terms")
x = int(input("Enter the value of x :: "))
n = int(input("Enter number of terms :: "))
total = 0
sign = 1  # alternates +, -
denominator = 1
for i in range(1, n + 1):
    term = (x**i) / denominator
    total += sign * term
    sign *= -1
    denominator += 2
print("--------------------Result--------------------")
print(f"Sum :: {total}")