### prime number

# ----------------------------------
# prime or not
print("----------------------------------------")
def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

number = 97
if isPrime(number):
    print(f"{number} is- Prime Number.")
else:
    print(f"{number} is- 'NOT a Prime'")


# --------------------------------------------
# primes till number
print("----------------------------------------")
def printPrimeNUmber(num):

    for i in range(2, num + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i, end=" ")

number = 100
printPrimeNUmber(number)


# -------------------------------------------------
# first n primes
print("\n----------------------------------------")
def printPrimesCount(count):
    num = 1
    while count >= 1:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            count -= 1

count = 7
printPrimesCount(count)
