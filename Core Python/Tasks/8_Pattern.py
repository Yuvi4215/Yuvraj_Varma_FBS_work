### user define row and columns values

row=int(input("Enter Rows value :: "))
column=int(input("Enter column value ::"))

for i in range(0, row):
    for j in range(0, column):
        print("*", end=" ")
    print()

print("------------------next-----------------")
for i in range(0, row):
    for j in range(0, column):
        if(i==0 or i==row-1 or j==0 or j==column-1):
            print("*", end=" ")
        else:
            print(" ", end= " ")
    print()

