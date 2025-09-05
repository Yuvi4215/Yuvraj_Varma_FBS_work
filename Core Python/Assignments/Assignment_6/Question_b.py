""" pattern
1 
2 3 
4 5 6 
7 8 9 10
"""
# rows= 4
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows :: "))
index = 1
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(index, end=" ")
        index += 1
    print()