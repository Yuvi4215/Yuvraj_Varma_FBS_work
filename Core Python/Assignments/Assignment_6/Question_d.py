"""pattern
A
A B
A B C
A B C D
A B C D E
"""
# rows=5
print("--------------------Start--------------------")
rows = int(input("Enter number of rows :: "))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    alphabet = 65
    for j in range(1, i + 1):
        print(chr(alphabet), end=" ")
        alphabet += 1
    print()