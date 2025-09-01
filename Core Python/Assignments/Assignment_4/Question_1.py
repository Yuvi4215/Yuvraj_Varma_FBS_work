### WAP to print all even numbers until n.

num = int(input("Enter the number ::"))
index = 2
while index <= num:
    if index % 2 == 0:
        print(index, end=" ")
    index += 2