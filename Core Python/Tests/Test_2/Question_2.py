## Question 2

# take 3-digit user input
num = int(input("Enter 3 digit number :: "))

# perform calculation
last_digit = num % 10
num = num // 10

middle_digit = num % 10
num = num // 10

first_digit = num % 10

# compare and Display the results
if first_digit / 2 == middle_digit and first_digit * 2 == last_digit:
    print("Yes, You have done it")
else:
    print("Please try next time.")
