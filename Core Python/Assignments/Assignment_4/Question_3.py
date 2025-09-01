### WAP to print sum of series upto n.

num = int(input("Enter the number ::"))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(f"Sum :: {sum}")