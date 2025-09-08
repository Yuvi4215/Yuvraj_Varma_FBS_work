### pattern
value = 0
for i in range(1, 6):
    for j in range(1, 6):
        if value == 0:
            value = 1
            print(value, end=" ")
        else:
            value = 0
            print(value, end=" ")
    print()
