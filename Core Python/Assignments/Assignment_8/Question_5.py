### WAP to print Sum of all prime numbers between 1 to n


def calculatePrimeSum(num):
    sum = 0
    for i in range(2, num + 1):
        flag = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i, end=" ")
            sum += i
    return sum


num = int(input("Enter the value of num: "))
result = calculatePrimeSum(num)
print(f"Sum of all prime numbers between 1 to {num} is: {result}")
