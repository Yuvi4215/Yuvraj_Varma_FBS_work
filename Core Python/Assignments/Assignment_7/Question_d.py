"""pattern
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5 
"""
#rows = 24
print("--------------------Start--------------------")
rows = int(input("Enter number of rows :: "))
print("--------------------Result--------------------")
for i in range(1, rows + 1):

    for j in range(1, rows + 1 - i):
        print(" ", end="  ")
    value = i
    for j in range(1, i + 1):
        if value>9:
            print(value, end=" ")
        else:
            print(value, end="  ")
        value += 1
    value = (i - 1) * 2
    for j in range(1, i):
        if value>9:
            print(value, end=" ")
        else:
            print(value, end="  ")
        value -= 1
    print()