"""pattern
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I 
"""
# rows=5
print("--------------------Start--------------------")
rows = int(input("Enter the number of rows ::"))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, rows + 1 - i):
        print(" ", end=" ")
    alphabet = 65
    for j in range(1, i * 2):
        print(chr(alphabet), end=" ")
        alphabet+=1
    print()