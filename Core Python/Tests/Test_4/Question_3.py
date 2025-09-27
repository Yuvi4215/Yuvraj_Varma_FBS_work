### 3. WAP to print following patterns :
#        * * * * * * * * *
#                      *
#                    *
#                  *
#                *
#              *
#            *
#          *
#        * * * * * * * * *


def printPattern(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == 1 or (i + j == num + 1) or i == num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


number = int(input("Enter the number : "))
printPattern(number)
