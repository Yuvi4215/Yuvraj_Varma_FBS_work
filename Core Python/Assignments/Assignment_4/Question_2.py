### WAP to print all odd numbers until n.

num = int(input("Enter the number ::"))
index = 1
while index <= num:
    if index % 2 != 0:
        print(index, end=" ")
    index += 2