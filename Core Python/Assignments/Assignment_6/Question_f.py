"""pattern
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
"""
# rows=5
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows ::"))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, rows + 1 - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        print(j, end=" ")
    print()