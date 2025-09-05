"""pattern
1 2 3 4 5 
2     5 
3   5 
4 5 
5 
"""
rows=5
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, rows + 2 - i):
        if i == 1:
            print(j, end=" ")
        elif j == 1:
            print(i, end=" ")
        elif i + j == rows + 1:
            print(rows, end=" ")
        else:
            print(" ", end=" ")
    print()