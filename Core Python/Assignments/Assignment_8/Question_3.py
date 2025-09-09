### Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


# A- series(1+ 2 + 3 + 4+..... + n)
def sumOfNaturalNum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


# B- series(1!+ 2! + 3! + 4!+..... + n!)
def sumOfFactorialNum(num):
    sum = 0
    for i in range(1, num + 1):
        factorial = 1
        for j in range(2, i + 1):
            factorial *= j
        sum += factorial

    return sum


# B- series(1^1 + 2^2 + 3^3+ ...... n^n)
def sumOfSelfPowerSeries(num):
    sum = 0
    for i in range(1, num + 1):
        power = 1
        for j in range(1, i + 1):
            power *= i
        sum += power
    return sum


print("----------Series- 1+ 2 + 3 + 4+..... + n----------")
num = int(input("Enter the value of n: "))
sum = sumOfNaturalNum(num)
print("--------------------Result--------------------")
print(f"Sum is :: {sum}")
print("--------------------End--------------------\n\n")


print("----------Series- 1!+ 2! + 3! + 4!+..... + n!----------")
num = int(input("Enter the value of n: "))
sum = sumOfFactorialNum(num)
print("--------------------Result--------------------")
print(f"Sum is :: {sum}")
print("--------------------End--------------------\n\n")


print("----------Series- 1^1 + 2^2 + 3^3+ ...... n^n----------")
num = int(input("Enter the value of n: "))
sum = sumOfSelfPowerSeries(num)
print("--------------------Result--------------------")
print(f"Sum is :: {sum}")
print("--------------------End--------------------\n\n")
