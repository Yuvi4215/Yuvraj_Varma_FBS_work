### Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + …..n!
print("--------------------Start--------------------")

print("a. 1! + 2! + 3! + 4! + …..n!")
num = int(input("Enter the number :: "))
n=num
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
n=num
total=0
for i in range(1,n+1):
    power=1
    for j in range(1,i+1):
        power*=j
    total+=power
print("--------------------Result--------------------")
print(f"Sum :: {total}")


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# print()
# print("c. Sum of a geometric series")
# n=int(input("Enter the number of terms :: "))
# common_ratio=int(input("Enter Common ratio :: "))
# total=0
# while n>0:
#     common_ratio*=common_ratio
#     n-=1
# total=common_ratio-1
# print("--------------------Result--------------------")
# print(f"Sum :: {total}")

# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + …. to n terms
