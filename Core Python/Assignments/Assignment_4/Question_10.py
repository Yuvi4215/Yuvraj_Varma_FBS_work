### WAP to check if given number is Perfect Number.
num = int(input("Enter the number ::"))
sum=0
for i in range(1, num ):
    if num%i  == 0 :
        sum+=i

if sum== num:
    print(f"It is perfect number-->The sum of divisor:{sum} and number:{num},  ")
else:
    print(f"It is not perfect Number.The sum of divisor:{sum} and number:{num}")