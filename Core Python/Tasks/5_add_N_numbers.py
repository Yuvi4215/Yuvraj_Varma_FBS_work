### WAP to add first N numbers

# Take N value from User
num = int(input("Enter the Number :: "))
total = 0
# using loop to add numbers

if num < 0:
    while num < 0:
        print(total)
        total += num
        num += 1
else:
    while num > 0:
        total += num
        num -= 1

# Display the result
print(f"first N number Sum is ::{total}")
