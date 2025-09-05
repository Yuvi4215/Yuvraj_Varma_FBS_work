""" pattern
* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * * 
"""
print("--------------------Start--------------------")
# size=6
size = int(input("Enter size of square pattern :: "))
print("--------------------Result--------------------")
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == 1 or i == size or j == 1 or j == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()