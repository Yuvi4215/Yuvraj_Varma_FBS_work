"""pattern
    * 
   * * 
  *   * 
 *     * 
*       * 
 *     * 
  *   * 
   * * 
    * 
"""
print("--------------------Start--------------------")
#rows = 24
rows = int(input("Enter number of rows :: "))
print("--------------------Result--------------------")
for i in range(1, rows + 1):
    for j in range(1, rows + 1 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        if j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1, rows):
    for j in range(1, i + 1):
        print(" ", end="")
    for j in range(1, rows + 1 - i):
        if j == 1 or i + j == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()