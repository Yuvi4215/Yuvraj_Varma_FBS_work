### WAP print Sum of all odd numbers between 1 to n


def calculateOddSum(nnum):
    sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:   
            sum += i
    return sum


num = int(input("Enter the value of n: "))
result = calculateOddSum(num)
print(f"Sum of all odd numbers between 1 to {num} is: {result}")
