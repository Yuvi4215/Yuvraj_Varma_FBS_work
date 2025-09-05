"""*Pascal's triangle pattern.
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
"""
# rows=5
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows ::"))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, rows + 1 - i):
        print(" ", end=" ")
    val = 1
    for j in range(1, i + 1):
        if len(str(val))>=3:
            print(val, end="  ")
        else:
            print(val, end="   ")
        val = val * (i - j) // j
    print()