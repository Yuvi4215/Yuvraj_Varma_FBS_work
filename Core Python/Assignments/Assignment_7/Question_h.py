"""pattern
1  -  -  -  -  -  -  -  1  
1  2  -  -  -  -  -  2  1  
1  2  3  -  -  -  3  2  1  
1  2  3  4  -  4  3  2  1  
1  2  3  4  5  4  3  2  1  
"""
#rows = 24
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows ::"))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j > 9:
            print(j, end=" ")
        else:
            print(j, end="  ")

    for j in range(1, rows + 1 - i):
        print("-", end="  ")
    for j in range(1, rows - i):
        print("-", end="  ")
    value = i
    for j in range(1, i + 1):
        if i == rows and j == 1:
            print("", end="")
            value -= 1
        else:
            if value > 9:
                print(value, end=" ")
            else:
                print(value, end="  ")
            value -= 1
    print()