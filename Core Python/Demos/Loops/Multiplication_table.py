### WAP to print a table of user defined number

#take number value from user
num=int(input("Enter the number :: "))

#program to print table
i=1
while i<=10:
    print(f"{i} -- {i*num}")
    i+=1