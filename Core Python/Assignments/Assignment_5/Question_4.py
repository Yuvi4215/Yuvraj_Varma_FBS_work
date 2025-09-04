### Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)
print("--------------------Start--------------------")
num = int(input("Enter the number ::"))
sum = 0
temp = num
count = len(str(num))

while temp > 0:
    digit = temp % 10
    temp = temp // 10
    sum += digit**count

print("--------------------Result--------------------")
if num == sum:
    print("It is an Armstrong number.")
else:
    print("It is Not an Armstrong number.")
print(f"Sum :: {sum}")