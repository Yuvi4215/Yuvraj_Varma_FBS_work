### Prime number functions using recursion

# ----------------------------------
# check-prime using recusrion
def isPrimeRecursion(num, index=2):
   
    if num <= 1:
        return False
    if index > int(num**0.5):
        return True
    if num % index == 0:
        return False
    return isPrimeRecursion(num, index + 1)


# ----------------------------------
# prime upto a number using recusrion
def primeUptoRecursion(num, current=2):

    if current > num:
        return False   
    if isPrimeRecursion(current):
        print(current, end=" ")
    primeUptoRecursion(num, current + 1)


# ----------------------------------
# first N primes using recusrion

def first_n_PrimesRecursion(num, current=2, count=0):

    if count == num:
        return False   
    if isPrimeRecursion(current):
        print(current, end=" ")
        first_n_PrimesRecursion(num, current + 1, count + 1)
    else:
        first_n_PrimesRecursion(num, current + 1, count)



# ----------------------- Run Code ------------------------
number = int(input("Enter the Numbers to check for prime:: "))
print(f"------------check prime for {number}-------------")
if isPrimeRecursion(number):
    print(f"{number} is- PRIME Number")
else:
    print(f"{number} is- NOT a Prime.")



number= int(input("\nEnter the last digit of range :: "))
print(f"------------Primes up to: {number} ------------")
primeUptoRecursion(number)



number= int(input("\n\nEnter how many prime numbers needed :: "))
print(f"\n------------First :{number} primes:------------")
first_n_PrimesRecursion(number)
