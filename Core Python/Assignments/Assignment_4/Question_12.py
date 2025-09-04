### WAP to print Armstrong number within a given range

start = int(input("Enter the start number of range ::"))
end = int(input("Enter the end number of range ::"))

flag = True

for num in range(start, end + 1):
    count = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        sum += digit**count
    if num == sum:
        flag = False
        print(f"Armstrong number found- {num}.")
if flag:
    print("There is no Armstrong number.")
