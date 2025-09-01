### WAP to check if a given number is prime number or not.

num = int(input("Enter the number ::"))
index = 2
if num < 2:
    print("enter number greater than 1.")
else:
    while index < num:
        if num % index == 0:
            print(f" {num} :: is not a Prime Number")
            break
        index += 1
    else:
        print(f" {num} :: is Prime Number.")