### 1. Write a function to which we pass a parameter and print the factors of a given number
# For Eg: Factors of 12 : 1,2,3,4,6,12


def printFactors(num):

    for ele in range(1, num + 1):
        if num % ele == 0:
            print(ele, end=" ")


number = int(input("Enter the number : "))
printFactors(number)