### WAP to print Armstrong number within a given range
num = int(input("Enter the number ::"))
sum = 0
temp = num
count = len(str(num))

while temp > 0:
    digit = temp % 10
    temp = temp // 10
    sum += digit**count

if num == sum:
    print("It is an Armstrong number.")
else:
    print("It is Not an Armstrong number.")
print(f"Sum :: {sum}")