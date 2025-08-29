### WAP to add digits from three digit number.
num = int(input("Enter only three digit Number:: "))

last = num % 10
num = num // 10

middle = num % 10
num = num // 10

first = num % 10
num = num // 10

print(
    f"sum of digit for 1st:{first}, 2nd:{middle} and 3rd:{last} is :: {first+middle+last}"
)
