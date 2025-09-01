### WAP to print all numbers in a range divisible by a given number.
num_range = int(input("Enter the number Range ::"))
num = int(input("Enter the number ::"))
for i in range(num, num_range + 1):
    if i % num == 0:
        print(i, end=" ")