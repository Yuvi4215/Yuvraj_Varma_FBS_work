"""pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
# rows= 24
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows :: "))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, rows):
    for j in range(1, rows + 1 - i):
        print("*", end=" ")
    print()