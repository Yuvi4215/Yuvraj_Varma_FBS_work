for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("-------------Next--------------")

for i in range(1,6):
    for j in range(1,6):
        if(i==j or i+j==6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("-------------Next--------------")

for i in range(1,6):
    for j in range(1,6):
        if(j==1 or j==5 or i==j or i+j==6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("-------------Next--------------")
for i in range(1,6):
    for j in range(1,i+1):
        if( j==1 or i==j or i==5):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1,6):
    for j in range(1,i):
        print(" ", end=" ")
    for j in range(1, 6+1-i):
        print("*", end=" ")
    print()