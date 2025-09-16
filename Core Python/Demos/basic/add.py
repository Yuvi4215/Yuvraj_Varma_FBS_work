#### Series x + X^2/2 + X^3/3 + X^4/4......+X^n/n


def getSumOfPower(digit, n):
    if n == 1:
        return digit

    return getPower(digit, n, n) + getSumOfPower(digit, n - 1)


def getPower(digit, n, current):
    if current == 1:
        return digit / n

    return digit * getPower(digit, n, current - 1)


num = int(input("Enter the x value :: "))
end = int(input("Enter the n value :: "))

sum = getSumOfPower(num, end)
print("Sum :: ", sum)