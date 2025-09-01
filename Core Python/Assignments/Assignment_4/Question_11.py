### WAP to check if given number Strong Number.

num = int(input("Enter the number ::"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    temp = temp // 10
    temp_sum = 1
    while digit > 1:
        temp_sum *= digit
        digit -= 1
    sum += temp_sum

if num == sum:
    print("It is a strong number.")
else:
    print("It is Not strong number.")
print(f"Sum :: {sum}")