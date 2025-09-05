"""pattern.
1  
1  2  
1     3  
1        4  
1  2  3  4  5 
"""
# rows = 24
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows ::"))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or i == rows or i == j:
            if j > 9:
                print(j, end=" ")
            else:
                print(j, end="  ")
        else:
            print(" ", end="  ")
    print()