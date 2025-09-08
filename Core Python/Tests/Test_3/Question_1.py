### print n prime number

number = 25
tem = 1
count = 0
while True:
    tem += 1
    for j in range(2, tem):
        if tem % j == 0:
            break
    else:
        print(tem)
        number -= 1
    if count == number:
        break