### Write a program to calculate the m to the power n using recursion.


def calculatePower(m, n):
    if n < 1:
        return 1
    return m * calculatePower(m, n - 1)


m = int(input("Enter the value for 'm' :: "))
n = int(input("Enter the value for 'n' :: "))

print(f"m^n value is : {calculatePower(m,n)}")